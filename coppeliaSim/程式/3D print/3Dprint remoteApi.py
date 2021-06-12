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
    print ('Conipconfigected to remote API server')
     
    res = vrep.simxAddStatusbarMessage(
        clientID, "40823214",
        vrep.simx_opmode_oneshot)
    if res not in (vrep.simx_return_ok, vrep.simx_return_novalue_flag):
        print("Could not add a message to the status bar.")
 

    opmode = vrep.simx_opmode_oneshot_wait
    STREAMING = vrep.simx_opmode_streaming

    vrep.simxStartSimulation(clientID, opmode)

    ret,joint1=vrep.simxGetObjectHandle(clientID,"X",opmode)
    ret,joint2=vrep.simxGetObjectHandle(clientID,"Y",opmode)
    ret,joint3=vrep.simxGetObjectHandle(clientID,"Z",opmode)
    dx=0
    dy=0
    dz=0
    dt=0.005
    cont=0
    rangeR=0.013
    max_h=0.35
    vrep.simxSetJointTargetPosition(clientID,joint1,dx,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint2,dx,opmode)
    vrep.simxSetJointTargetPosition(clientID,joint3,dx,opmode)

    while True:
        #Clockwise
        if keyboard.is_pressed("8"):
            dx=dx+dt
            cont=float(math.pow(dx,2)+math.pow(dy,2))
            if cont<rangeR:
                vrep.simxSetJointTargetPosition(clientID,joint1,dx,opmode)
                print(dx,dy,dz)
            else:
                print("Out of range")
                dx=dx-dt
        if keyboard.is_pressed("2"):
            dx=dx-dt
            cont=float(math.pow(dx,2)+math.pow(dy,2))
            if cont<rangeR:
                vrep.simxSetJointTargetPosition(clientID,joint1,dx,opmode)
                print(dx,dy,dz)
            else:
                print("Out of range")
                dx=dx+dt
        if keyboard.is_pressed("4"):
            dy=dy+dt
            cont=float(math.pow(dx,2)+math.pow(dy,2))
            if cont<rangeR:
                vrep.simxSetJointTargetPosition(clientID,joint2,dy,opmode)
                print(dx,dy,dz)
            else:
                print("Out of range")
                dy=dy-dt
        if keyboard.is_pressed("6"):
            dy=dy-dt
            cont=float(math.pow(dx,2)+math.pow(dy,2))
            if cont<rangeR:
                vrep.simxSetJointTargetPosition(clientID,joint2,dy,opmode)
                print(dx,dy,dz)
            else:
                print("Out of range")
                dy=dy+dt
        if keyboard.is_pressed("space"):    
            dz=dz+dt   
            if dz<max_h:       
                vrep.simxSetJointTargetPosition(clientID,joint3,dz,opmode)
                print(dx,dy,dz)
            else:
                print("too high")
                dz=dz-dt 
        if keyboard.is_pressed("c"):
            dz=dz-dt
            if dz<0:
                print("too low")
                dz=0
            else:
                vrep.simxSetJointTargetPosition(clientID,joint3,dz,opmode)
                print(dx,dy,dz)
    else:
        print ('Failed connecting to remote API server')
        print ('End')