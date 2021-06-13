function moving(x,y)
    --[[
    This code is write by 40823214
    The way i find the angle is finding the intersect of the two arm
    One center is base on the robot arm center 
    Other center is at the target we set
    So know we konw the distance between the target and the center(code name c)
    And two arms' length(code name a,b)
    as long as we find the Three sides of the triangle(a,b,c)
    and we can know the angle and every corner
    ]]
    a=0.467
    b=0.401
    c=math.pow(math.pow(x,2)+math.pow(y,2),0.5)
    s=(a+b+c)*0.5
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
    print(deg3)
    sim.setJointTargetPosition(joint1,deg1)
    sim.setJointTargetPosition(joint2,-deg2)
    sim.setJointTargetPosition(joint3,deg3)
    
end

function pick_and_place(x,y)
    sim.setIntegerSignal("pad_switch",0)
    sim.wait(t)
    moving(0,0.868)
    sim.wait(t)
    moving(x,y)
    sim.wait(t)
    sim.setIntegerSignal("pad_switch",1)
    sim.setJointTargetPosition(jointz,-0.055)
    sim.wait(t)
    sim.setJointTargetPosition(jointz,0)
    sim.wait(t)
end

function sysCall_threadmain()
    t=5
    joint1=sim.getObjectHandle('joint1')
    joint2=sim.getObjectHandle('joint2')
    jointz=sim.getObjectHandle('jointZ')
    joint3=sim.getObjectHandle('joint3')
    sim.setJointTargetPosition(joint1,0)
    sim.setJointTargetPosition(joint2,0)
    sim.setJointTargetPosition(joint3,0)
    sim.setIntegerSignal("pad_switch",1)
    sim.setJointTargetPosition(jointz,-0.055)
    sim.wait(t)
    sim.setJointTargetPosition(jointz,0)
    sim.wait(t)
    while sim.getSimulationState()~=sim.simulation_advancing_abouttostopre do
        x=0.2
        y=0.7
        moving(x,y)
        sim.wait(t)
        pick_and_place(x,y)
        x=-0.3
        y=-0.55
        moving(x,y)
        sim.wait(t)
        pick_and_place(x,y)
    end
end