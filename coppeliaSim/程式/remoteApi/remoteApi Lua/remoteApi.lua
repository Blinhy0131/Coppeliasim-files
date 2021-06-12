
client = simx.start('192.168.192.1', 19997, True, True, 5000, 5)

function sysCall_init()
    joint01=sim.getObjectHandle('joint1')
    joint02=sim.getObjectHandle('joint2')
    joint03=sim.getObjectHandle('joint3')
    joint04=sim.getObjectHandle('joint4')
    joint05=sim.getObjectHandle('joint5')
    joint06=sim.getObjectHandle('joint6')
    jointJW1=sim.getObjectHandle('jointJW01')
    jointJW2=sim.getObjectHandle('jointJW02')
    degset01=0
    degset02=0
    degset03=0
    degset04=0
    degset05=0
    degset06=0
    degsetJW1=0
    degsetJW2=0
    dif=1
    balance_contral=true
    cont=1
    --degset001={"degset11","degset12","degset13","degset14","degset15"}
    --degset002={"degset21","degset22","degset23","degset24","degset25"}
    --degset003={"degset31","degset32","degset33","degset34","degset35"}
    --degset004={"degset41","degset42","degset43","degset44","degset45"}
    --degset005={"degset51","degset52","degset53","degset54","degset55"}
    Cam1=sim.getObjectHandle('cam01')
    Cam2=sim.getObjectHandle('cam02')
    CamView1=sim.floatingViewAdd(0.9,0.9,0.2,0.2,0)
    CamView2=sim.floatingViewAdd(0.7,0.9,0.2,0.2,0)
    sim.adjustView(CamView1,Cam1,64)
    sim.adjustView(CamView2,Cam2,64)
end

function sysCall_cleanup()
    sim.floatingViewRemove(CamView1)
    sim.floatingViewRemove(CamView2)
end

function sysCall_actuation()
    message,auxiliaryData=sim.getSimulatorMessage()
    while message~=-1 do
        if (message==sim.message_keypress) then

            if  (auxiliaryData[1]==48) then
                if (balance_contral==true)then
                    balance_contral=false
                else
                    balance_contral=true
                end
            end

            if (auxiliaryData[1]==2009) then
                degset01=degset01+dif
                sim.setJointTargetPosition(joint01,degset01*math.pi/180)
            end
            if (auxiliaryData[1]==2010) then
                degset01=degset01-dif
                sim.setJointTargetPosition(joint01,degset01*math.pi/180)
            end
            if (auxiliaryData[1]==2007) then
                degset02=degset02+dif
                sim.setJointTargetPosition(joint02,degset02*math.pi/180)
            end
            if (auxiliaryData[1]==2008) then
                degset02=degset02-dif
                sim.setJointTargetPosition(joint02,degset02*math.pi/180)
            end
            if (auxiliaryData[1]==56) then
                degset03=degset03+dif
                sim.setJointTargetPosition(joint03,degset03*math.pi/180)
            end
            if (auxiliaryData[1]==50) then
                degset03=degset03-dif
                sim.setJointTargetPosition(joint03,degset03*math.pi/180)

            end
            if (auxiliaryData[1]==54) then
                degset04=degset04+dif
                sim.setJointTargetPosition(joint04,degset04*math.pi/180)
            end
            if (auxiliaryData[1]==52) then
                degset04=degset04-dif
                sim.setJointTargetPosition(joint04,degset04*math.pi/180)
            end
            if (auxiliaryData[1]==49) then
                degset05=degset05+dif
                sim.setJointTargetPosition(joint05,degset05*math.pi/180)
            end
            if (auxiliaryData[1]==55) then
                degset05=degset05-dif
                sim.setJointTargetPosition(joint05,degset05*math.pi/180)
            end
            if (auxiliaryData[1]==51) then
                degset06=degset06-dif
                sim.setJointTargetPosition(joint06,degset06*math.pi/180)
            end
            if (auxiliaryData[1]==57) then
                degset06=degset06+dif
                sim.setJointTargetPosition(joint06,degset06*math.pi/180)
            end


            if (auxiliaryData[1]==43) then
                degsetJW1=degsetJW1+1
                degsetJW2=degsetJW2-1
                sim.setJointTargetPosition(jointJW1,degsetJW1*math.pi/180)
                sim.setJointTargetPosition(jointJW2,degsetJW2*math.pi/180)
            end
            if (auxiliaryData[1]==45) then
                degsetJW1=degsetJW1-1
                degsetJW2=degsetJW2+1
                sim.setJointTargetPosition(jointJW1,degsetJW1*math.pi/180)
                sim.setJointTargetPosition(jointJW2,degsetJW2*math.pi/180)
            end

            if (balance_contral==true) then
                if (auxiliaryData[1]==2008) then
                degset03=degset03-dif
                sim.setJointTargetPosition(joint03,degset03*math.pi/180)
                end
                if (auxiliaryData[1]==2007) then
                degset03=degset03+dif
                sim.setJointTargetPosition(joint03,degset03*math.pi/180)
                end
            end
            --[[if  (auxiliaryData[1]==46) then
                if (JAW_contral==true)then
                    JAW_contral=false
                else
                    JAW_contral=true
                end
            end--]]

            --[[if (auxiliaryData[1]==99) then
                if (cont<=5) then
                    degset001[1]=degset01
                    degset002[1]=degset01
                    degset003[1]=degset01
                    degset004[1]=degset01
                    degset005[1]=degset01
                    cont=cont+1
                else
                    print(wrong)
                end
            end
            if (auxiliaryData[1]==32) then
                sim.setJointTargetPosition(joint01,degset001[1]*math.pi/180)

                sim.setJointTargetPosition(joint02,degset002[1]*math.pi/180)
                function sleep(2)
                    if n > 0 then os.execute("ping -n " .. tonumber(n+1) .. " localhost > NUL") end
                end
                sim.setJointTargetPosition(joint03,degset003[1]*math.pi/180)
                function sleep(2)
                    if n > 0 then os.execute("ping -n " .. tonumber(n+1) .. " localhost > NUL") end
                end
                sim.setJointTargetPosition(joint04,degset004[1]*math.pi/180)
                function sleep(2)
                    if n > 0 then os.execute("ping -n " .. tonumber(n+1) .. " localhost > NUL") end
                end
                sim.setJointTargetPosition(joint05,degset005[1]*math.pi/180)
                function sleep(2)
                    if n > 0 then os.execute("ping -n " .. tonumber(n+1) .. " localhost > NUL") end
                end

            end--]]

        end
        message,auxiliaryData=sim.getSimulatorMessage()
    end
end
