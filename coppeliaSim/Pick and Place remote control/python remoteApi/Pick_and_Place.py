import sim as vrep
import math
import random
import time
import math

def rotate_motor(x,y,z,switch):
    x=float(x)
    y=float(y)
    z=float(z)
    deg1=math.atan(x/(1.415-y))
    x=1.415-(1.415-y)/math.cos(deg1)
    length=math.pow((math.pow(0.2,2)+math.pow(1.082,2)),0.5)
    distance=math.pow((math.pow(1.082-x,2)+math.pow(0.96-z,2)),0.5)
    perimeter=(length+distance+0.76)/2
    area=math.pow(perimeter*(perimeter-length)*(perimeter-distance)*(perimeter-0.76),0.5)
    high=2*area/distance
    joint2_after_sita=math.asin(high/0.76)
    joint2_zero_sita=math.atan((1.082-x)/(0.96-z))
    deg2=joint2_after_sita-joint2_zero_sita
    joint3_base=math.atan(1.082/0.2)
    angle_joint3=math.acos(high/length)
    deg3=(90*math.pi/180)+joint2_after_sita-angle_joint3-joint3_base
    deg4=deg2-deg3
    if switch==1:
        vrep.simxSetJointTargetPosition(clientID,joint01,deg1,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint02,deg2,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint03,(-deg3),opmode)
        vrep.simxSetJointTargetPosition(clientID,joint04,(-deg4),opmode)
    if switch==2:
        vrep.simxSetJointTargetPosition(clientID,joint03,(-deg3),opmode)
        time.sleep(0.2)
        vrep.simxSetJointTargetPosition(clientID,joint01,deg1,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint02,deg2,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint04,(-deg4),opmode)

def signal_switch(singal):

    if singal==1 :
        vrep.simxSetIntegerSignal(clientID,"call_1",1,opmode) #here might have a error
    if singal==2 :
        vrep.simxSetIntegerSignal(clientID,"call_2",1,opmode)
    if singal==3 :
        vrep.simxSetIntegerSignal(clientID,"call_3",1,opmode)
    if singal==4 :
        vrep.simxSetIntegerSignal(clientID,"call_4",1,opmode)
    if singal==5 :
        vrep.simxSetIntegerSignal(clientID,"call_5",1,opmode)
    if singal==6 :
        vrep.simxSetIntegerSignal(clientID,"call_6",1,opmode)
    if singal==12:
        vrep.simxSetIntegerSignal(clientID,'call_1',0,opmode) #here might have a error
    if singal==11:
        vrep.simxSetIntegerSignal(clientID,"call_2",0,opmode)
    if singal==10:
        vrep.simxSetIntegerSignal(clientID,"call_3",0,opmode)
    if singal==9:
        vrep.simxSetIntegerSignal(clientID,"call_4",0,opmode)
    if singal==8:
        vrep.simxSetIntegerSignal(clientID,"call_5",0,opmode)
    if singal==7:
        vrep.simxSetIntegerSignal(clientID,"call_6",0,opmode)

def clean():
    vrep.simxSetIntegerSignal(clientID,"call_1",0,opmode)
    vrep.simxSetIntegerSignal(clientID,"call_2",0,opmode)
    vrep.simxSetIntegerSignal(clientID,"call_3",0,opmode)
    vrep.simxSetIntegerSignal(clientID,"call_4",0,opmode)
    vrep.simxSetIntegerSignal(clientID,"call_5",0,opmode)
    vrep.simxSetIntegerSignal(clientID,"call_6",0,opmode)

print ('Start')
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
  
if clientID != -1:
    print ('Connected to remote API server')
      
    res = vrep.simxAddStatusbarMessage(
        clientID, "pad testing",
        vrep.simx_opmode_oneshot)
    if res not in (vrep.simx_return_ok, vrep.simx_return_novalue_flag):
        print("Could not add a message to the status bar.")
  
     
    opmode = vrep.simx_opmode_oneshot_wait
    STREAMING = vrep.simx_opmode_streaming
  
     
    vrep.simxStartSimulation(clientID, opmode)
    ret,joint01=vrep.simxGetObjectHandle(clientID,"joint1",opmode)
    ret,joint02=vrep.simxGetObjectHandle(clientID,"joint2",opmode)
    ret,joint03=vrep.simxGetObjectHandle(clientID,"joint3",opmode)
    ret,joint04=vrep.simxGetObjectHandle(clientID,"joint4",opmode)
    ret,jointr=vrep.simxGetObjectHandle(clientID,"Rotate",opmode)
    tt=1.5
    long_t=3
    long_long_t=3 #time set
    rotate_deg=0 #pad rotate
    atz=0  #altitude set
    setx=-0.5
    setpx=0.5 #center pick set
    sety=0.16
    setpy=0.16 #center fall set
    cube=1              # set cube
    ball_pick_time=0    #total ball we pick
    ball_put_time=31     #total ball we put
    put_cont=0          # print the ball we put
    pick_high=['0.0645','0.134','0.202','0.2785'] #pick up high set
    fall_high=['0.05','0.12','0.18','0.26'] #fall high set
    high_up=['0','0','0.05','0.12']

    
    

    while True :
        clean() #clean all the 
        vrep.simxSetJointTargetPosition(clientID,joint01,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint02,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint03,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint04,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,jointr,0,opmode)
        time.sleep(tt)
        for ball in range(1,7,1):
            ball_pick_time=ball_pick_time+1 #total time we pick
            i=1
            unit=0
            level=0
            while level < ball_pick_time :  #find which level and place should be of the xy coordinates
                unit=unit+1
                level=level+unit**2
            finding_XY=ball_pick_time  #this is the XY on that floor
            while i<=unit-1:
                finding_XY=finding_XY-(i**2) 
                i=i+1
            X_Pos=finding_XY%unit  #the X and Y coordinates(by balls)
            if X_Pos==0:
                X_Pos=unit
            Y_Pos=(math.ceil(finding_XY/unit)) 
            BaseX=setx-((unit-1)*0.05)#now we need to find the 0 of the xy
            BaseY=sety-((unit-1)*0.05)
            #vrep.simxSetJointTargetPosition(clientID,joint01,BaseX+(0.1*(X_Pos-1)),opmode)
            #time.sleep(tt)
            rotate_motor(BaseX+(0.1*(X_Pos-1)),BaseY+(0.1*(Y_Pos-1)),high_up[(unit-1)],1)
            time.sleep(tt)
            print("Picking up the ball nember",ball_pick_time,"...")
            signal_switch(ball)
            rotate_motor(BaseX+(0.1*(X_Pos-1)),BaseY+(0.1*(Y_Pos-1)),pick_high[(unit-1)],1)
            time.sleep(tt)
            rotate_motor(BaseX+(0.1*(X_Pos-1)),BaseY+(0.1*(Y_Pos-1)),high_up[(unit-1)],2)
            time.sleep(tt)
            rotate_deg=rotate_deg+60
            vrep.simxSetJointTargetPosition(clientID,jointr,rotate_deg*math.pi/180,opmode)
            time.sleep(tt)
        vrep.simxSetJointTargetPosition(clientID,joint01,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint02,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint03,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,joint04,0,opmode)
        vrep.simxSetJointTargetPosition(clientID,jointr,0,opmode)
        time.sleep(tt)
        for ball in range(1,7,1):
            ball_put_time=ball_put_time-1 #total time we put
            put_cont=put_cont+1
            i=1
            unit=0
            level=0
            while level < ball_put_time :
                unit=unit+1
                level=level+unit**2
            finding_XY=ball_put_time 
            while i<=unit-1:
                finding_XY=finding_XY-(i**2) 
                i=i+1
            X_Pos=finding_XY%unit
            if X_Pos==0:
                X_Pos=unit
            Y_Pos=(math.ceil(finding_XY/unit)) 
            BaseX=setpx-((unit-1)*0.05)#now we need to find the 0 of the xy
            BaseY=setpy-((unit-1)*0.05)
            rotate_deg=rotate_deg-60
            vrep.simxSetJointTargetPosition(clientID,jointr,rotate_deg*math.pi/180,opmode)
            time.sleep(tt)
            rotate_motor(BaseX+(0.1*(X_Pos-1)),BaseY+(0.1*(Y_Pos-1)),high_up[(unit-1)],1)
            time.sleep(tt)
            print("Putting the ball nember",put_cont,"...")
            rotate_motor(BaseX+(0.1*(X_Pos-1)),BaseY+(0.1*(Y_Pos-1)),fall_high[(unit-1)],1)
            time.sleep(tt)
            signal_switch((ball+6))
            time.sleep(0.5)
            rotate_motor(BaseX+(0.1*(X_Pos-1)),BaseY+(0.1*(Y_Pos-1)),high_up[(unit-1)],1)
            time.sleep(tt)
        if ball_pick_time==30:
            pick_high=['0.07','0.135','0.207','0.278']
            setx=-setx
            setpx=-setpx
            ball_pick_time=0
            ball_put_time=31
            put_cont=0