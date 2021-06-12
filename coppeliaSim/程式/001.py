
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

if clientID != -1:
    print ('Connected to remote API server')

    res = vrep.simxAddStatusbarMessage(
        clientID, "40823218",
        vrep.simx_opmode_oneshot)
    if res not in (vrep.simx_return_ok, vrep.simx_return_novalue_flag):
        print("Could not add a message to the status bar.")

    # Communication operating mode with the remote API : wait for its answer before continuing (blocking mode)
    # http://www.coppeliarobotics.com/helpFiles/en/remoteApiConstants.htm
    opmode = vrep.simx_opmode_oneshot_wait
    STREAMING = vrep.simx_opmode_streaming

    # Try to retrieve motors and robot handlers
    # http://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm#simxGetObjectHandle
    vrep.simxStartSimulation(clientID, opmode)
    ret,base_handle=vrep.simxGetObjectHandle(clientID,"joint1",opmode)
    ret,bottom_handle=vrep.simxGetObjectHandle(clientID,"joint2",opmode)
    ret,top_handle=vrep.simxGetObjectHandle(clientID,"joint3",opmode)
    ret,rotate_handle=vrep.simxGetObjectHandle(clientID,"joint4",opmode)
    ret,wrist_handle=vrep.simxGetObjectHandle(clientID,"joint5",opmode)
    while True:
        #Clockwise
        if keyboard.is_pressed("1"):
         vrep.simxSetJointTargetVelocity(clientID,base_handle,0.1,opmode)
        #anti-Clockwise
        if keyboard.is_pressed("f"):
         vrep.simxSetJointTargetVelocity(clientID,base_handle,-0.1,opmode)
        #bottom_handle up
        if keyboard.is_pressed ("w"):
         vrep.simxSetJointTargetVelocity(clientID,bottom_handle,0.1,opmode)
        #bottom_handle down
        if keyboard.is_pressed ("s"):
         vrep.simxSetJointTargetVelocity(clientID,bottom_handle,-0.1,opmode)
         #top_handle up
        if keyboard.is_pressed ("e"):
         vrep.simxSetJointTargetVelocity(clientID,top_handle,0.1,opmode)
         #top_handle down
        if keyboard.is_pressed ("d"):
         vrep.simxSetJointTargetVelocity(clientID,top_handle,-0.1,opmode)
         #rotate
        if keyboard.is_pressed ("r"):
         vrep.simxSetJointTargetVelocity(clientID,rotate_handle,0.1,opmode)
         #wrist_handle left
        if keyboard.is_pressed ("j"):
         vrep.simxSetJointTargetVelocity(clientID,wrist_handle,0.1,opmode)
         #wrist_handle right
        if keyboard.is_pressed ("k"):
         vrep.simxSetJointTargetVelocity(clientID,wrist_handle,-0.1,opmode)
         #stop
        if keyboard.is_pressed ("space"):
         vrep.simxSetJointTargetVelocity(clientID,base_handle,0,opmode)
         vrep.simxSetJointTargetVelocity(clientID,bottom_handle,0,opmode)
         vrep.simxSetJointTargetVelocity(clientID,top_handle,0,opmode)
         vrep.simxSetJointTargetVelocity(clientID,rotate_handle,0,opmode)
         vrep.simxSetJointTargetVelocity(clientID,wrist_handle,0,opmode)


else:
    print ('Failed connecting to remote API server')
    print ('End')
