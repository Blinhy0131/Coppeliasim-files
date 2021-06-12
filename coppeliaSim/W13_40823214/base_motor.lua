function moving(x,y,z)
    deg1=math.atan(x/(1.082-y)) --rad
    sim.getJointTargetPosition(joint01,deg1)
    x=1082-(1082-y)/math.cos(deg1)
    --deg2=math.asim((math.pow((math.pow((1.082-x),2)+math.pow((0.96-z),2)-math.pow(1.082,2)-math.pow(0.2,2)-math.pow(0.76,2))/2,0.5))/2)-atan((960-z)/(1082-x))
    sim.getJointTargetPosition(joint02,deg2)
    deg3=90*180/math.pi-math.atan(1.082/0.2)+math.atan(0.96-z/1.082-x)-math.acos(math.pow((math.pow((1.082-x),2)+math.pow((0.96-z),2)-math.pow(1.082,2)-math.pow(0.2,2)-math.pow(0.76,2)),0.5)/math.pow(math.pow(1.082,2)+math.pow(0.2,2),0.5))
    sim.getJointTargetPosition(joint03,deg3)
    deg4=deg2-deg1
    sim.getJointTargetPosition(joint04,deg4)
end

function signal_switch(singal,enable)
    
    if singal==1 or singal==12 then
        sim.setIntegerSignal("call_1",enable)
    end
    if singal==2 or singal==11 then
        sim.setIntegerSignal("call_2",enable)
    end
    if singal==3 or singal==10 then
        sim.setIntegerSignal("call_3",enable)
    end
    if singal==4 or singal==9 then
        sim.setIntegerSignal("call_4",enable)
    end
    if singal==5 or singal==8 then
        sim.setIntegerSignal("call_5",enable)
    end
    if singal==6 or singal==7 then
        sim.setIntegerSignal("call_6",enable)
    end
end

function sysCall_init()
    joint01=sim.getObjectHandle('joint1')
    joint02=sim.getObjectHandle('joint2')
    joint03=sim.getObjectHandle('joint3')
    joint04=sim.getObjectHandle('joint4')
    jointr=sim.getObjectHandle('Rotate')
    dif=0.01
    x=0
    y=0
    z=0
    balance_contral=true
end

function sysCall_actuation()
    message,auxiliaryData=sim.getSimulatorMessage()
    while message~=-1 do
        if (message==sim.message_keypress) then
            if (auxiliaryData[1]==2009) then
                x=x+dif
                moving(x,y,z)
            end
            if (auxiliaryData[1]==2009) then
                x=x-dif
                moving(x,y,z)
            end
            if (auxiliaryData[1]==2007) then
                y=y+dif
                moving(x,y,z)
            end
            if (auxiliaryData[1]==2008) then
                y=y-dif
                moving(x,y,z)
            end
        end
    message,auxiliaryData=sim.getSimulatorMessage()
    end
end

