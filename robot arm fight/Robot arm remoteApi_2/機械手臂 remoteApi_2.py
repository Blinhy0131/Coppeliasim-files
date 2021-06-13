import sim as vrep
import math
import random
import time
import keyboard
import math
#from winsound import Beep
 
  
print ('Start')
  
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19998, True, True, 5000, 5)
  
if clientID != -1:
    print ('Connected to remote API server')
      
    res = vrep.simxAddStatusbarMessage(
        clientID, "control_2",
        vrep.simx_opmode_oneshot)
    if res not in (vrep.simx_return_ok, vrep.simx_return_novalue_flag):
        print("Could not add a message to the status bar.")
  
     
    opmode = vrep.simx_opmode_oneshot_wait
    STREAMING = vrep.simx_opmode_streaming
  
     
    vrep.simxStartSimulation(clientID, opmode)
    ret,joint01=vrep.simxGetObjectHandle(clientID,"joint11",opmode)
    ret,joint02=vrep.simxGetObjectHandle(clientID,"joint22",opmode)
    ret,joint03=vrep.simxGetObjectHandle(clientID,"joint33",opmode)
    ret,joint04=vrep.simxGetObjectHandle(clientID,"joint44",opmode)
    ret,joint05=vrep.simxGetObjectHandle(clientID,"joint55",opmode)
    ret,joint06=vrep.simxGetObjectHandle(clientID,"joint66",opmode)
    degset01=0
    degset02=0
    degset03=0
    degset04=0
    degset05=0
    degset06=0
    dif=0.5
    balance_contral=True
    
    while True:
        if keyboard.is_pressed("left"):
            degset01=degset01+dif
            vrep.simxSetJointTargetPosition(clientID,joint01,degset01*math.pi/180,opmode)
        if keyboard.is_pressed("right"):
            degset01=degset01-dif
            vrep.simxSetJointTargetPosition(clientID,joint01,degset01*math.pi/180,opmode)
        if keyboard.is_pressed("up"):
            degset02=degset02+dif
            vrep.simxSetJointTargetPosition(clientID,joint02,degset02*math.pi/180,opmode)
        if keyboard.is_pressed("down"):
            degset02=degset02-dif
            vrep.simxSetJointTargetPosition(clientID,joint02,degset02*math.pi/180,opmode)
        if keyboard.is_pressed("8"):
            degset03=degset03+dif
            vrep.simxSetJointTargetPosition(clientID,joint03,degset03*math.pi/180,opmode)
        if keyboard.is_pressed("2"):
            degset03=degset03-dif
            vrep.simxSetJointTargetPosition(clientID,joint03,degset03*math.pi/180,opmode)
        if keyboard.is_pressed("6"):
            degset04=degset04+dif
            vrep.simxSetJointTargetPosition(clientID,joint04,degset04*math.pi/180,opmode)
        if keyboard.is_pressed("4"):
            degset04=degset04-dif
            vrep.simxSetJointTargetPosition(clientID,joint04,degset04*math.pi/180,opmode)
        if keyboard.is_pressed("1"):
            degset05=degset05+dif
            vrep.simxSetJointTargetPosition(clientID,joint05,degset05*math.pi/180,opmode)
        if keyboard.is_pressed("7"):
            degset05=degset05-dif
            vrep.simxSetJointTargetPosition(clientID,joint05,degset05*math.pi/180,opmode)
        if keyboard.is_pressed("3"):
            degset06=degset06+dif
            vrep.simxSetJointTargetPosition(clientID,joint05,degset05*math.pi/180,opmode)
        if keyboard.is_pressed("9"):
            degset06=degset06-dif
            vrep.simxSetJointTargetPosition(clientID,joint06,degset06*math.pi/180,opmode)
        if keyboard.is_pressed("0"):
            if balance_contral==True:
                balance_contral=False
            if balance_contral==False:
                balance_contral=True