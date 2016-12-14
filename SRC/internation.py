import MySQLdb
import numpy
from math import radians, cos, sin, asin, sqrt 
from dijkstra import dijkstra
from salesman import run

db = MySQLdb.connect("localhost","root","123","BIGPJ" )
cursor = db.cursor()
sql = "SELECT * FROM distance"
sql2= "SELECT * FROM connect"
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
        if i!=j and (connect[i*di+j][4]!=None):
            g[i][j]=haversine(row[4],row[5],row[6],row[7])

D=numpy.zeros((di,di))

for i in range(0,di):
	A,B=dijkstra(g,i)
	for j in range(0,di):
		D[i][j]=A[j]


route=run(Din=D)
for i in route:
	print(connect[i][2],connect[i][3],connect[i][4])

#tsp=TSP(Din=D)
#tsp.run(100000)
#print tsp.ga.best.gene

db.close()
