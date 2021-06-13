import sim as vrep
import math
import random
import time
 
 
 
 
 
vrep.simxFinish(-1) #終止所有連接
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5) #設立一個連接口19997(默認地址)
 
#啟動模擬
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
if clientID!= -1:
    print ('Conexion establecida')
 
else:
    print('Connection not successful')
    sys.exit('Could not connect')