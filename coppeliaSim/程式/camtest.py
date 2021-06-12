import sim as vrep

print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)
if clientID!=-1:
    print ('Connected to remote API server')
    vrep.simxReadStringStream(clientID,"dvsData",vrep.simx_opmode_streaming)   

    while vrep.simxGetConnectionId(clientID) != -1:
        res,signal=vrep.simxReadStringStream(clientID,"dvsData",vrep.simx_opmode_buffer)   
        if res == vrep.simx_return_novalue_flag:
            # no events yet
            pass
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')