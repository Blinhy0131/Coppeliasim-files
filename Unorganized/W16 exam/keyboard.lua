function sysCall_init()
    joint1=sim.getObjectHandle('joint1')
    joint2=sim.getObjectHandle('joint2')
    jointz=sim.getObjectHandle('jointZ')
    joint3=sim.getObjectHandle('joint3')
    sim.setJointTargetPosition(joint1,0)
    sim.setJointTargetPosition(joint2,0)
    sim.setJointTargetPosition(joint3,0)
    sim.setJointTargetPosition(jointz,0)
    deg1=0
    deg2=0
    deg3=0
end

function sysCall_actuation()
    message,auxiliaryData=sim.getSimulatorMessage()
    while message~=-1 do
        if (message==sim.message_keypress) then
            if (auxiliaryData[1]==2009) then
            deg1=deg1+1
            deg3=deg2-deg1
            sim.setJointTargetPosition(joint1,deg1*math.pi/180)
            end
            if (auxiliaryData[1]==2010) then
            deg1=deg1-1
            deg3=deg2-deg1
            sim.setJointTargetPosition(joint1,deg1*math.pi/180)
            end
            if (auxiliaryData[1]==2007) then
            deg2=deg2+1
            deg3=deg1-deg2
            sim.setJointTargetPosition(joint2,deg2*math.pi/180)
            end
            if (auxiliaryData[1]==2008) then
            deg2=deg2-1
            deg3=deg1-deg2
            sim.setJointTargetPosition(joint2,deg2*math.pi/180)
            end
            if (auxiliaryData[1]==115) then
                sim.setJointTargetPosition(jointz,-0.055)
                sim.setIntegerSignal("pad_switch",1)
            end
            if(auxiliaryData[1]==119) then
                sim.setJointTargetPosition(jointz,0)
            end
            if(auxiliaryData[1]==32) then
                sim.setIntegerSignal("pad_switch",0)
            end
            sim.setJointTargetPosition(joint3,deg3*math.pi/180)
        end
    message,auxiliaryData=sim.getSimulatorMessage()
    end
end
