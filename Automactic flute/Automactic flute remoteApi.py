import sim as vrep
import math
import random
import time
import keyboard
import math
#from winsound import Beep

 
print ('Start')
 

vrep.simxFinish(-1)

clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
 
if clientID != -1:
    print ('Connected to remote API server')
     
    res = vrep.simxAddStatusbarMessage(
        clientID, "test-25",
        vrep.simx_opmode_oneshot)
    if res not in (vrep.simx_return_ok, vrep.simx_return_novalue_flag):
        print("Could not add a message to the status bar.")
 
    
    opmode = vrep.simx_opmode_oneshot_wait
    STREAMING = vrep.simx_opmode_streaming
 
    
    vrep.simxStartSimulation(clientID, opmode)
    ret,joint1=vrep.simxGetObjectHandle(clientID,"Revolute3_1",opmode)
    ret,joint2=vrep.simxGetObjectHandle(clientID,"Revolute3_2",opmode)
    ret,joint3=vrep.simxGetObjectHandle(clientID,"Revolute3_3",opmode)
    ret,joint4=vrep.simxGetObjectHandle(clientID,"Revolute3_4",opmode)
    ret,joint5=vrep.simxGetObjectHandle(clientID,"Revolute3_5",opmode)
    ret,joint6=vrep.simxGetObjectHandle(clientID,"Revolute3_6",opmode)

    ret,joint01=vrep.simxGetObjectHandle(clientID,"joint0_1",opmode)
    ret,joint02=vrep.simxGetObjectHandle(clientID,"joint0_2",opmode)
    ret,joint03=vrep.simxGetObjectHandle(clientID,"joint0_3",opmode)
    ret,joint04=vrep.simxGetObjectHandle(clientID,"joint0_4",opmode)
    ret,joint05=vrep.simxGetObjectHandle(clientID,"joint0_5",opmode)
    ret,joint06=vrep.simxGetObjectHandle(clientID,"joint0_6",opmode)

    degr=-12*math.pi/180
    py=0.05
    set1=False
    set2=False
    set3=False
    set4=False
    set5=False
    set6=False

    vrep.simxSetJointTargetPosition(clientID,joint1,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint01,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint2,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint02,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint3,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint03,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint4,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint04,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint5,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint05,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint6,0,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint06,0,opmode)

    while True:
        
        if keyboard.is_pressed("f"):
            if set1==False:
                vrep.simxSetJointTargetPosition(clientID,joint1,degr,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint01,py,opmode)
                set1=True
        if keyboard.is_pressed("d"):
            if set2==False:
                vrep.simxSetJointTargetPosition(clientID,joint2,degr,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint02,py,opmode)
                set2=True
        if keyboard.is_pressed("s"):
            if set3==False:
                vrep.simxSetJointTargetPosition(clientID,joint3,degr,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint03,py,opmode)
                set3=True
        if keyboard.is_pressed("j"):
            if set4==False:
                vrep.simxSetJointTargetPosition(clientID,joint4,degr,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint04,py,opmode)
                set4=True
        if keyboard.is_pressed("k"):
            if set5==False:
                vrep.simxSetJointTargetPosition(clientID,joint5,degr,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint05,py,opmode)
                set5=True
        if keyboard.is_pressed("l"):
            if set6==False:
                vrep.simxSetJointTargetPosition(clientID,joint6,degr,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint06,py,opmode)
                set6=True

        
        if keyboard.is_pressed("r"):
            if set1==True:
                vrep.simxSetJointTargetPosition(clientID,joint1,0,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint01,0,opmode)
                set1=False
        if keyboard.is_pressed("e"):
            if set2==True:
                vrep.simxSetJointTargetPosition(clientID,joint2,0,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint02,0,opmode)
                set2=False
        if keyboard.is_pressed("w"):
            if set3==True:
                vrep.simxSetJointTargetPosition(clientID,joint3,0,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint03,0,opmode)
                set3=False
        if keyboard.is_pressed("u"):
            if set4==True:
                vrep.simxSetJointTargetPosition(clientID,joint4,0,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint04,0,opmode)
                set4=False
        if keyboard.is_pressed("i"):
            if set5==True:
                vrep.simxSetJointTargetPosition(clientID,joint5,0,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint05,0,opmode)
                set5=False
        if keyboard.is_pressed("o"):
            if set6==True:
                vrep.simxSetJointTargetPosition(clientID,joint6,0,opmode)
                vrep.simxSetJointTargetPosition(clientID,joint06,0,opmode)
                set6=False
        
        #if(set1==true ):
            #Beep(422, 3000) 
        
 
 
else:
    print ('Failed connecting to remote API server')
    print ('End')