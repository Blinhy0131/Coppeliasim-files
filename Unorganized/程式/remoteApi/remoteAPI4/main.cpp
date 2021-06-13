#include <Windows.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI acos(-1)

extern "C" {
    #include "remoteAPI/extApi.h"
}



using namespace std;

int main(){
    int clientID = 0;
    simxFinish(-1);                                                     //! Close any previously unfinished business
    clientID = simxStart((simxChar*)"127.0.0.1", 19997, true, true, 5000, 5);  //!< Main connection to V-REP
    Sleep(1);
    if (clientID != -1)
    {
        char[] joint1;
        simxGetObjectHandle(clientID,(const simxChar*) "joint1",(simxInt *) &Joint1, (simxInt) simx_opmode_oneshot_wait)
        int degset01=-11.9;
        int degset02=34.69;
        int degset03=-20.2;
        int degset04=-11.9;
        int degset05=-11.9;
        int dif=1;
        simxSetJointTargetPosition(joint01,degset01*(PI / 180));
        simxSetJointTargetPosition(joint02,degset02*(PI / 180));
        simxSetJointTargetPosition(joint03,degset03*(PI / 180));
        simxSetJointTargetPosition(joint04,degset04*(PI / 180));
        simxSetJointTargetPosition(joint05,degset05*(PI / 180));
        bool balance_contral=true;


        clientID,auxiliaryData=simGetSimulatorMessage();


        while (clientID!=-1) {
            if (clientID==sim.message_keypress) {
                if (auxiliaryData[1]==2009) {
                    degset01=degset01+dif;
                    simxSetJointTargetPosition(joint01,degset01*(PI / 180));
                }
                if (auxiliaryData[1]==2010) {
                    degset01=degset01-dif;
                simxSetJointTargetPosition(joint01,degset01*(PI / 180));
                }
                if (auxiliaryData[1]==2007) {
                    degset02=degset02+dif;
                    simxSetJointTargetPosition(joint02,degset02*(PI / 180));
                }
                if (auxiliaryData[1]==2008) {
                    degset02=degset02-dif;
                    simxSetJointTargetPosition(joint02,degset02*(PI / 180));
                }
                if (auxiliaryData[1]==56) {
                    degset03=degset03+dif;
                    simxSetJointTargetPosition(joint03,degset03*(PI / 180));
                }
                if (auxiliaryData[1]==50) {
                    degset03=degset03-dif;
                    simxSetJointTargetPosition(joint03,degset03*(PI / 180));

                }
                if (auxiliaryData[1]==54) {
                    degset04=degset04+dif;
                    simxSetJointTargetPosition(joint04,degset04*(PI / 180));
                }
                if (auxiliaryData[1]==52) {
                    degset04=degset04-dif;
                    simxSetJointTargetPosition(joint04,degset04*(PI / 180));
                }
                if (auxiliaryData[1]==49) {
                    degset05=degset05+dif;
                    simxSetJointTargetPosition(joint05,degset05*(PI / 180))
                }
                if (auxiliaryData[1]==51) {
                    degset05=degset05-dif;
                    simxSetJointTargetPosition(joint05,degset05*(PI / 180));
                }




                if  (auxiliaryData[1]==48){
                    if (balance_contral==true){
                        balance_contral=false;
                    }else{
                        balance_contral=true;
                    }
                }
                if (balance_contral==true) {
                    if (auxiliaryData[1]==2007) {
                        degset03=degset03+dif ;
                        simxSetJointTargetPosition(joint03,degset03*(PI / 180));
                    }
                    if (auxiliaryData[1]==2008) {
                        degset03=degset03-dif;
                        simxSetJointTargetPosition(joint03,degset03*(PI / 180));
                        }
                    }
                }
        clientID,auxiliaryData=simGetSimulatorMessage();
        }
    }
    simxFinish(clientID);
    return clientID;
}
