import MySQLdb
import numpy
from math import radians, cos, sin, asin, sqrt 
from dijkstra import dijkstra
from salesman import run

db = MySQLdb.connect("localhost","root","123","BIGPJ" )
cursor = db.cursor()
sql = "SELECT * FROM FRdistance"
sql2= "SELECT * FROM FRconnect"
def haversine(lat1,lon1,lat2,lon2): 

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  

    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 
    return c * r 

cursor.execute(sql)
result = cursor.fetchall()
cursor.execute(sql2)
connect = cursor.fetchall()
di=int(sqrt(len(result)))
g={}


for i in range(0,di):
    g[i]={}
    for j in range(0,di):
        row=result[i*di+j]
        if i!=j :
            g[i][j]=haversine(row[4],row[5],row[6],row[7])

D=numpy.zeros((di,di))


for i in range(0,di):
	for j in range(0,di):
		if i==j:
			D[i][j]=0
		else:
			D[i][j]=g[i][j]

route=run(Din=D)
for i in route:
	print(connect[i][3],connect[i][4],connect[i][5],connect[i][6])


db.close()
