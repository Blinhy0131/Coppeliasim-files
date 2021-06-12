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
    opmode = vrep.simx_opmode_oneshot_wait
    STREAMING = vrep.simx_opmode_streaming
    vrep.simxStartSimulation(clientID, opmode)

