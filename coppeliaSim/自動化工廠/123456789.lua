--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function sysCall_init() 
    -- User Parameters
    beltSpeed = 0.4
    T_insert = 1
    insertCoordinate =  {-1.3,-0.55,0.25}
    goodPercentage = 0.19
    goodColor = {0,1,0}   
--------------------------------------------------------------------------
    -- Initialize auxiliary variables
    T_last_inserted = 0
    deltaTime = 0 -- the time of picking up the box
    hasStopped = false -- means belt is running
    boxList = {}
    boxDummyList = {}
    boolList = {}
--------------------------------------------------------------------------
    -- Initialize handles, set beltSpeed
    box = sim.getObjectHandle("Box")
    boxDummy = sim.getObjectHandle("BoxDummy")

    forwarder=sim.getObjectHandle('ConveyorBelt_forwarder')
    -- cone shaped sensor at the end of 1st belt to detect object and its color
    proximity = sim.getObjectHandle("Proximity_sensor0")
    -- Access to 2nd conveyor belt script
    belt2script = sim.getScriptHandle("customizableConveyor")
    -- set conveyorBeltVelocity to beltSpeed
    sim.setScriptSimulationParameter(sim.handle_self,"conveyorBeltVelocity",beltSpeed)

    -- Insert the first box during initializiation
    insertBox()
end
--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function sysCall_cleanup() 
 
end 
--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function sysCall_actuation() 
    beltVelocity=sim.getScriptSimulationParameter(sim.handle_self,"conveyorBeltVelocity")
    
    -- Here we "fake" the transportation pads with a single static rectangle that we dynamically reset
    -- at each simulation pass (while not forgetting to set its initial velocity vector) :
    
    relativeLinearVelocity={beltVelocity,0,0}
    -- Reset the dynamic rectangle from the simulation (it will be removed and added again)
    sim.resetDynamicObject(forwarder)
    -- Compute the absolute velocity vector:
    m=sim.getObjectMatrix(forwarder,-1)
    m[4]=0 -- Make sure the translation component is discarded
    m[8]=0 -- Make sure the translation component is discarded
    m[12]=0 -- Make sure the translation component is discarded
    absoluteLinearVelocity=sim.multiplyVector(m,relativeLinearVelocity)
    -- Now set the initial velocity of the dynamic rectangle:
    sim.setObjectFloatParameter(forwarder,sim.shapefloatparam_init_velocity_x,absoluteLinearVelocity[1])
    sim.setObjectFloatParameter(forwarder,sim.shapefloatparam_init_velocity_y,absoluteLinearVelocity[2])
    sim.setObjectFloatParameter(forwarder,sim.shapefloatparam_init_velocity_z,absoluteLinearVelocity[3])
end 
--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function sysCall_sensing() 
    -- Read Proximity sensor1 (0= nothing detected, 1 = object detected)
    local res = sim.readProximitySensor(proximity)
    print(res)
    -- Check if possible to insert an new box
    if (sim.getSimulationTime()-T_last_inserted > T_insert) and not hasStopped then
        insertBox()
    end

    -- If proximity sensor detects an object, stop the belt, stop inserting objects
    if res == 1  then
        -- boolList[1]==true means sensor detected the favorite object
        sim.setScriptSimulationParameter(sim.handle_self,"conveyorBeltVelocity",0)
        if boolList[1] then
           
            deltaTime = sim.getSimulationTime()-T_last_inserted
            hasStopped = true

	    -- Generate new pickupPath
            --updatePickupPath(boxDummyList[1])
	    -- Remove first object and dummy handle from table
            --objs = removeFirstObject()
	    -- Set pickupDummy-handle in robot script
            --sim.setScriptVariable("pickupDummy",robotScriptHandle,objs[2])
	    -- Set a signal such that robot knows that object is available
            --sim.setIntegerSignal("objectAvailable",1)
        end
    end

    -- If proximity sensor detects nothing and belt has stopped, start belt, continue inserting
    if res == 0 then
        sim.clearIntegerSignal("objectAvailable")
        sim.setScriptSimulationParameter(sim.handle_self,"conveyorBeltVelocity",beltSpeed)
        hasStopped = false
        T_last_inserted = sim.getSimulationTime()-deltaTime
    end
end
--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function insertBox()
    -- Generate random numbers

    local disturbedCoordinates = {0,0,0}
 
    -- Copy and paste box and boxDummy
    local insertedObjects = sim.copyPasteObjects({box,boxDummy},0)

    -- Update last inserted box time
    T_last_inserted = sim.getSimulationTime()

    -- Move and rotate
    sim.setObjectPosition(insertedObjects[1],-1,insertCoordinate)
  
    -- Store handles to boxes and dummies
    table.insert(boxList,insertedObjects[1])
    table.insert(boxDummyList,insertedObjects[2]) 

    -- Decide if object is good or bad
    local decision = math.random() 
    if decision <= goodPercentage then
	-- Object is good, assign goodColor
        sim.setShapeColor(insertedObjects[1],nil,sim.colorcomponent_ambient_diffuse,goodColor)
        table.insert(boolList,true)
    else
	-- Object is bad, assign random color
        sim.setShapeColor(insertedObjects[1],nil,sim.colorcomponent_ambient_diffuse,{1,0,0})
        table.insert(boolList,false)
    end
end
