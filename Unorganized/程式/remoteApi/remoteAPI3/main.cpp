#include <Windows.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


extern "C" {
    #include "remoteAPI/extApi.h"
}



using namespace std;

int main(){
    int clientID = 0;
    simxFinish(-1);
    clientID = simxStart((simxChar*)"127.0.0.1", 19997, true, true, 5000, 5);
    Sleep(1);
    if (clientID != -1)
    {
        int joint01;
        int joint02;
        int joint03;
        int joint04;
        int joint05;
        simxGetObjectHandle(clientID, "joint1", &joint01, simx_opmode_oneshot_wait);//setting
        simxGetObjectHandle(clientID, "joint2", &joint02, simx_opmode_oneshot_wait);
        simxGetObjectHandle(clientID, "joint3", &joint03, simx_opmode_oneshot_wait);
        simxGetObjectHandle(clientID, "joint4", &joint04, simx_opmode_oneshot_wait);
        simxGetObjectHandle(clientID, "joint5", &joint05, simx_opmode_oneshot_wait);


        float degset01=-11.9;
        float degset02=34.69;
        float degset03=-20.2;
        float degset04=-11.9;
        float degset05=-11.9;
        float dif=1;

        //angle set0
        simxSetJointTargetPosition(clientID,joint01,degset01,simx_opmode_oneshot);
        simxSetJointTargetPosition(clientID,joint02,degset02,simx_opmode_oneshot);
        simxSetJointTargetPosition(clientID,joint03,degset03,simx_opmode_oneshot);
        simxSetJointTargetPosition(clientID,joint04,degset04,simx_opmode_oneshot);
        simxSetJointTargetPosition(clientID,joint05,degset05,simx_opmode_oneshot);
        bool balance_contral=true;


        clientID,auxiliaryData=simGetSimulatorMessage();


        while (clientID!=-1) {
            if (clientID==simxmessage_keypress) {
                if (auxiliaryData[1]==2009) { //up Key
                    degset01=degset01+dif;
                    simxSetJointTargetPosition(clientID,joint01,degset01,simx_opmode_oneshot);
                }
                if (auxiliaryData[1]==2010) { //down key
                    degset01=degset01-dif;
                    simxSetJointTargetPosition(clientID,joint01,degset01,simx_opmode_oneshot);
                }
                if (auxiliaryData[1]==2007) { //left key
                    degset02=degset02+dif;
                    simxSetJointTargetPosition(clientID,joint02,degset02,simx_opmode_oneshot);
                }
                if (auxiliaryData[1]==2008) {  //right key
                    degset02=degset02-dif;
                    simxSetJointTargetPosition(clientID,joint02,degset02,simx_opmode_oneshot);
                }
                if (auxiliaryData[1]==56) { //num8 key
                    degset03=degset03+dif;
                    simxSetJointTargetPosition(clientID,joint03,degset03,simx_opmode_oneshot);
                }
                if (auxiliaryData[1]==50) { //num2 key
                    degset03=degset03-dif;
                    simxSetJointTargetPosition(clientID,joint03,degset03,simx_opmode_oneshot);

                }
                if (auxiliaryData[1]==54) { //num6 key
                    degset04=degset04+dif;
                    simxSetJointTargetPosition(clientID,joint04,degset04,simx_opmode_oneshot);
                }
                if (auxiliaryData[1]==52) { //num4 key
                    degset04=degset04-dif;
                    simxSetJointTargetPosition(clientID,joint04,degset04,simx_opmode_oneshot);
                }
                if (auxiliaryData[1]==49) { //mun1 key
                    degset05=degset05+dif;
                    simxSetJointTargetPosition(clientID,joint05,degset05,simx_opmode_oneshot);
                }
                if (auxiliaryData[1]==51) { //num3 key
                    degset05=degset05-dif;
                    simxSetJointTargetPosition(clientID,joint05,degset05,simx_opmode_oneshot);
                }




                if  (auxiliaryData[1]==48){ //setting auto Balance at num0 key
                    if (balance_contral==true){
                        balance_contral=false;
                    }else{
                        balance_contral=true;
                    }
                }
                if (balance_contral==true) {
                    if (auxiliaryData[1]==2007) {
                        degset03=degset03+dif ;
                        simxSetJointTargetPosition(clientID,joint03,degset03,simx_opmode_oneshot);
                    }
                    if (auxiliaryData[1]==2008) {
                        degset03=degset03-dif;
                        simxSetJointTargetPosition(clientID,joint03,degset03,simx_opmode_oneshot);
                        }
                    }
                }
        clientID,auxiliaryData=simGetSimulatorMessage();
        }
    }
    simxFinish(clientID);
    return clientID;
}
