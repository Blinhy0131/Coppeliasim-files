--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function sysCall_init() 
    -- User Parameters
    beltSpeed = 0.04
    T_insert = 1
    insertCoordinate = {-1.3,-0.5,0.25}
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
    proximity = sim.getObjectHandle("Proximity_sensor")
    -- Access to 2nd conveyor belt script
    belt2script = sim.getScriptHandle("customizableConveyor")
    -- set conveyorBeltVelocity to beltSpeed
    sim.setScriptSimulationParameter(sim.handle_self,"conveyorBeltVelocity",beltSpeed)
---------------------------------------------------------------------------
-- Supported functions are added at the end of this script
-- (1) inserBox()
-- (2) createPath
-- (3) updatePickupPath
-- (4) removeFirstObject

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

    -- Check if possible to insert an new box
    if (sim.getSimulationTime()-T_last_inserted > T_insert) and not hasStopped then
        insertBox()
    end

    -- If proximity sensor detects an object, stop the belt, stop inserting objects
    if res == 1 and not hasStopped then
        -- boolList[1]==true means sensor detected the favorite object
        if boolList[1] then
            sim.setScriptSimulationParameter(sim.handle_self,"conveyorBeltVelocity",0)
            deltaTime = sim.getSimulationTime()-T_last_inserted
            hasStopped = true

	    -- Generate new pickupPath
            updatePickupPath(boxDummyList[1])
	    -- Remove first object and dummy handle from table
            objs = removeFirstObject()
	    -- Set pickupDummy-handle in robot script
            sim.setScriptVariable("pickupDummy",robotScriptHandle,objs[2])
	    -- Set a signal such that robot knows that object is available
            sim.setIntegerSignal("objectAvailable",1)
        --[[else
            local box = table.remove(boxList,1)
            local boxDummy = table.remove(boxDummyList,1)
            table.remove(boolList,1)

            sim.removeObject(Box)
            sim.removeObject(BoxDummy)--]]
        end
    end

    -- If proximity sensor detects nothing and belt has stopped, start belt, continue inserting
    if res == 0 and hasStopped then
        sim.clearIntegerSignal("objectAvailable")
        sim.setScriptSimulationParameter(sim.handle_self,"conveyorBeltVelocity",beltSpeed)
        hasStopped = false
        T_last_inserted = sim.getSimulationTime()-deltaTime
    end
end
--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function removeFirstObject()
    -- Obtain handles by removing from tables
    local box = table.remove(boxList,1)
    local boxDummy = table.remove(boxDummyList,1)
    table.remove(boolList,1)

    -- Add handles to the belt2 tables
    sim.callScriptFunction("addObject",belt2script,{box,boxDummy})

    -- Return handles
    return {box,boxDummy}
end


function createPath(name,startPoint,startOrient,endPoint,endOrient)
    -- Create Path Object
    local path = sim.createPath(1)

    -- Create buffer variables
    local buffer = {startPoint[1],startPoint[2],startPoint[3],startOrient[1],startOrient[2],startOrient[3], 1,0,0,0,0,
                    endPoint[1],endPoint[2],endPoint[3],endOrient[1],endOrient[2],endOrient[3],             1,0,0,0,0}

    -- Insert 2 control points (start and endpoint)
    sim.insertPathCtrlPoints(path,0,0,2,buffer)

    -- Rename the object
    sim.setObjectName(path,name)
    -- Return handle to path
    return path
end
function insertBox()
    -- Generate random numbers
    local rand1 = math.random()
    local rand2 = math.random()
    local rand3 = math.random()

    -- Generate random disturbances on position and orientation
    local dx = (2*rand1-1)*0.1
    local dy = (2*rand2-1)*0.1
    local dphi = (2*rand3-1)*0.5
    local disturbedCoordinates = {0,0,0}
    disturbedCoordinates[1] = insertCoordinate[1]+dx
    disturbedCoordinates[2] = insertCoordinate[2]+dy
    disturbedCoordinates[3] = insertCoordinate[3]

    -- Copy and paste box and boxDummy
    local insertedObjects = sim.copyPasteObjects({box,boxDummy},0)

    -- Update last inserted box time
    T_last_inserted = sim.getSimulationTime()

    -- Move and rotate
--    sim.setObjectPosition(insertedObjects[1],-1,disturbedCoordinates)
    sim.setObjectPosition(insertedObjects[1],-1,insertCoordinate)
    sim.setObjectOrientation(insertedObjects[1],-1,{0,0,dphi})
  
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
function updatePickupPath(dummy)
    -- Obtain handle to last pickupPath
    local path = sim.getObjectHandle("pickupPath")
    -- Remove the path
    sim.removeObject(path)
    -- Obtain position of dummy to be reached
    local dummyPos = sim.getObjectPosition(dummy,-1)
    -- Obtain orientation of dummy to be reached
    local dummyOrient = sim.getObjectOrientation(dummy,-1)
    -- Create new path
    createPath("pickupPath",idlePos,idleOrient,dummyPos,dummyOrient)
end