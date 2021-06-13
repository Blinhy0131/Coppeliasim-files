function moving(x,y)
    a=0.4
    b=0.4
    c=math.pow((math.pow(x,2)+math.pow(y,2)),0.5)
    s=(a+b+c)/2
    area=math.pow((s*(s-a)*(s-b)*(s-c)),0.5)
    h=area/(2*c)
    deg1_base=math.atan(x/y)
    if x<0 and y<0 then
        deg1_base=deg1_base+math.pi
    end
    deg1_tri=math.asin(h/a)
    deg1=deg1_base+deg1_tri
    deg2=math.pi-(0.5*math.pi-deg1_tri)-math.acos(h/b)
    deg3=deg2-deg1
    print(deg1)
    sim.setJointTargetPosition(joint01,deg1)
    sim.setJointTargetPosition(joint02,-deg2)
    sim.setJointTargetPosition(joint03,deg3)
end


function sysCall_threadmain()
    t=5
    joint01=sim.getObjectHandle('joint1')
    joint02=sim.getObjectHandle('joint2')
    joint03=sim.getObjectHandle('joint3')
    jointz=sim.getObjectHandle('jointz')
    sim.setJointTargetPosition(joint01,0)
    sim.setJointTargetPosition(joint02,0)
    sim.setJointTargetPosition(joint03,0)
    sim.wait(t)
    sim.wait(t)
    sim.setIntegerSignal("pad_switch",1)
    sim.setJointTargetPosition(jointz,-0.04)
    sim.wait(t)
    sim.setJointTargetPosition(jointz,0)
    sim.wait(t)
    while sim.getSimulationState()~=sim.simulation_advancing_abouttostopre do
        moving(0.2,0.7)
        sim.wait(t)
        sim.setIntegerSignal("pad_switch",0)
        sim.wait(t)
        sim.setIntegerSignal("pad_switch",1)
        sim.wait(t)
        sim.setJointTargetPosition(jointz,-0.04)
        sim.wait(t)
        sim.setJointTargetPosition(jointz,0)
        sim.wait(t)
        moving(-0.3,-0.55)
        sim.wait(t)
        sim.setIntegerSignal("pad_switch",0)
        sim.wait(t)
        sim.setIntegerSignal("pad_switch",1)
        sim.wait(t)
        sim.setJointTargetPosition(jointz,-0.05)
        sim.wait(t)
        sim.setJointTargetPosition(jointz,0)
        sim.wait(t)
    end
end
