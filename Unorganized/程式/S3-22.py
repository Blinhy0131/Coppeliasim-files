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
        clientID, "40823242",
        vrep.simx_opmode_oneshot)
         
    if res not in (vrep.simx_return_ok, vrep.simx_return_novalue_flag):
        print("Could not add a message to the status bar.")
         
    opmode = vrep.simx_opmode_oneshot_wait
    vrep.simxStartSimulation(clientID, opmode)
    ret,vertical_handle=vrep.simxGetObjectHandle(clientID,"1",opmode)#設定軸對應名稱
    ret,spirit_handle=vrep.simxGetObjectHandle(clientID,"2",opmode)
    ret,cam_handle=vrep.simxGetObjectHandle(clientID,"3",opmode)
    while True:
        #keyboard "w" 前進
     if keyboard.is_pressed("w"):
            print("You pressed w")
           
            vrep.simxSetJointTargetVelocity(clientID,vertical_handle,1,opmode)
     if keyboard.is_pressed("s"):#keyboard "s" 後退
            print("You pressed s")
           
            vrep.simxSetJointTargetVelocity(clientID,vertical_handle,-1,opmode)
     if keyboard.is_pressed("a"):#keyboard "a"向左 
            print("You pressed a")
           
            vrep.simxSetJointTargetVelocity(clientID,spirit_handle,0.1,opmode)
     if keyboard.is_pressed("q"):#keyboard "d" 向右
            print("You pressed q")
           
            vrep.simxSetJointTargetVelocity(clientID,spirit_handle,-0.1,opmode)
     if keyboard.is_pressed("x"):#keyboard "q" 前進後退停止
            print("You pressed x")
           
            vrep.simxSetJointTargetVelocity(clientID,vertical_handle,0,opmode)
     if keyboard.is_pressed("z"):#keyboard "e" 左右停止
            print("You pressed z")
           
            vrep.simxSetJointTargetVelocity(clientID,spirit_handle,0,opmode) 
     if keyboard.is_pressed("e"):#keyboard "r" 凸輪轉動
            print("You pressed e")
           
            vrep.simxSetJointTargetVelocity(clientID,cam_handle,1,opmode)   
     if keyboard.is_pressed("d"):#keyboard "f" 凸輪停止
            print("You pressed d")
           
            vrep.simxSetJointTargetVelocity(clientID,cam_handle,-1,opmode)
     if keyboard.is_pressed("c"):#keyboard "f" 凸輪停止
            print("You pressed c")
           
            vrep.simxSetJointTargetVelocity(clientID,cam_handle,0,opmode)       
else:
    print ('Failed connecting to  remote API server')
print ('End')