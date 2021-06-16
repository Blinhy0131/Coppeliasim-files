import sim as vrep
import math
import random
import time
import math

def moving(x,y):
    a=0.467
    b=0.401
    c=math.pow(math.pow(x,2)+math.pow(y,2),0.5)
    s=(a+b+c)*0.5
    area=math.pow((s*(s-a)*(s-b)*(s-c)),0.5)
    h=2*area/c
    deg1_base=math.atan(x/y)
    if x<0 and y<0 :
        deg1_base=deg1_base+math.pi
    deg1_tri=math.asin(h/a)
    deg1=deg1_base+deg1_tri
    deg2=math.pi-(0.5*math.pi-deg1_tri)-math.acos(h/b)
    deg3=deg2-deg1
    vrep.simxSetJointTargetPosition(clientID,joint01,deg1,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint02,(-deg2),opmode)
    vrep.simxSetJointTargetPosition(clientID,joint03,deg3,opmode)

def pick_and_place(x,y):
    vrep.simxSetIntegerSignal(clientID,"pad_switch",0,opmode)
    time.sleep(tt)
    moving(0,0.868)
    time.sleep(tt)
    moving(x,y)
    time.sleep(tt)
    vrep.simxSetIntegerSignal(clientID,"pad_switch",1,opmode)
    vrep.simxSetJointTargetPosition(clientID,jointz,-0.055,opmode)
    time.sleep(tt)
    vrep.simxSetJointTargetPosition(clientID,jointz,0,opmode)
    time.sleep(tt)



print ('Start')
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
  
if clientID != -1:
    print ('Connected to remote API server')
    res = vrep.simxAddStatusbarMessage(
        clientID, "This is teach by 40823214 ",
        vrep.simx_opmode_oneshot)
    if res not in (vrep.simx_return_ok, vrep.simx_return_novalue_flag):
        print("Could not add a message to the status bar.")
  
     
    opmode = vrep.simx_opmode_oneshot_wait
    STREAMING = vrep.simx_opmode_streaming
  
     
    vrep.simxStartSimulation(clientID, opmode)
    ret,joint01=vrep.simxGetObjectHandle(clientID,"joint01",opmode)
    ret,joint02=vrep.simxGetObjectHandle(clientID,"joint02",opmode)
    ret,joint03=vrep.simxGetObjectHandle(clientID,"joint03",opmode)
    ret,jointz=vrep.simxGetObjectHandle(clientID,"jointZ",opmode)
    tt=0.5
 

    while True :
        vrep.simxSetJointTargetPosition(clientID,joint01,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint02,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint03,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,jointz,-0.055,opmode)
        vrep.simxSetIntegerSignal(clientID,"pad_switch",1,opmode)
        time.sleep(tt)
        vrep.simxSetJointTargetPosition(clientID,jointz,0,opmode)
        time.sleep(tt)
        while True:
            x=0.2
            y=0.7
            moving(x,y)
            time.sleep(tt)
            pick_and_place(x,y)
            x=-0.3
            y=-0.55
            moving(x,y)
            time.sleep(tt)
            pick_and_place(x,y)
