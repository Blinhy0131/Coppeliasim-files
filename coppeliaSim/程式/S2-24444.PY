import sim as vrep
import math
import random
import time
import keyboard
 
print ('Start')
 
# Close eventual old connections
vrep.simxFinish(-1)
# Connect to V-REP remote server
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
  
if clientID !=-1:
    print ('Connected to remote API server')
   
    res = vrep.simxAddStatusbarMessage(
        clientID, "40823204",
        vrep.simx_opmode_oneshot)
          
    if res not in (vrep.simx_return_ok, vrep.simx_return_novalue_flag):
        print("Could not add a message to the status bar.")
          
    opmode = vrep.simx_opmode_oneshot_wait
    STREAMING = vrep.simx_opmode_streaming
     
    vrep.simxStartSimulation(clientID, opmode)
    
    
    ret,fwheel_handle=vrep.simxGetObjectHandle(clientID,"joint0",opmode)
    ret,bwheel_handle=vrep.simxGetObjectHandle(clientID,"joint2",opmode)
    ret,pole1_handle=vrep.simxGetObjectHandle(clientID,"joint3",opmode)
    ret,pole2_handle=vrep.simxGetObjectHandle(clientID,"joint4",opmode)
    ds=0
    dy=0
    df=0
    db=0
    vrep.simxSetJointTargetPosition(clientID,fwheel_handle,df,opmode)
    vrep.simxSetJointTargetPosition(clientID,bwheel_handle,db,opmode)
    vrep.simxSetJointTargetPosition(clientID,pole1_handle,ds,opmode)
    vrep.simxSetJointTargetPosition(clientID,pole2_handle,dy,opmode)
    
    
    while True:
        #Clockwise
        if keyboard.is_pressed("2"):
            ds=ds-10
            dy=dy-10
            vrep.simxSetJointTargetPosition(clientID,pole1_handle,ds,opmode)
            vrep.simxSetJointTargePosition(clientID,pole2_handle,dy,opmode)
            print("up")
        if keyboard.is_pressed("4"):
            ds=ds+10
            dy=dy+10
            vrep.simxSetJointTargetPosition(clientID,pole1_handle,ds,opmode)
            vrep.simxSetJointTargetPosition(clientID,pole2_handle,dy,opmode)
            print("down")
        if keyboard.is_pressed("6"):
            df=df+30
            db=db+30
            vrep.simxSetJointTargetPosition(clientID,fwheel_handle,df,opmode)
            vrep.simxSetJointTargetPosition(clientID,bwheel_handle,db,opmode)
            print("left")
        if keyboard.is_pressed("8"):
            df=df-30
            db=db-30
            vrep.simxSetJointTargetPosition(clientID,fwheel_handle,df,opmode)
            vrep.simxSetJointTargetPosition(clientID,bwheel_handle,db,opmode)
            print("right")


             
else:
    print ('Failed connecting to  remote API server')
    print ('End')
