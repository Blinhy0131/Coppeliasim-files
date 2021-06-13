extern "C" {
    #include "Headers/exApi.h"
}

using namespace std;

int main(int argc,char **argv){

    string severIP = "127.0.0.1";
    int severPort = 19997;





   joint01=simxGetObjectHandle('joint1');
    joint02=simxGetObjectHandle('joint2');
    joint03=simxGetObjectHandle('joint3');
    joint04=simxGetObjectHandle('joint4');
    joint05=simxGetObjectHandle('joint5');
    int degset01=-11.9;
    int degset02=34.69;
    int degset03=-20.2;
    int degset04=-11.9;
    int degset05=-11.9;
    int dif=1;
    simxSetJointTargetPosition(joint01,degset01*math.pi/180);
    simxSetJointTargetPosition(joint02,degset02*math.pi/180);
    simxSetJointTargetPosition(joint03,degset03*math.pi/180);
    simxSetJointTargetPosition(joint04,degset04*math.pi/180);
    simxSetJointTargetPosition(joint05,degset05*math.pi/180);
    int balance_contral=true;


    message,auxiliaryData=simGetSimulatorMessage();


    while (message~=-1) {
        if (message==sim.message_keypress) {
            if (auxiliaryData[1]==2009) {
                degset01=degset01+dif;
                simxSetJointTargetPosition(joint01,degset01*math.pi/180);
            }
            if (auxiliaryData[1]==2010) {
                degset01=degset01-dif;
                simxSetJointTargetPosition(joint01,degset01*math.pi/180);
            }
            if (auxiliaryData[1]==2007) {
                degset02=degset02+dif;
                simxSetJointTargetPosition(joint02,degset02*math.pi/180);
            }
            if (auxiliaryData[1]==2008) {
                degset02=degset02-dif;
                simxSetJointTargetPosition(joint02,degset02*math.pi/180);
            }
            if (auxiliaryData[1]==56) {
                degset03=degset03+dif;
                simxSetJointTargetPosition(joint03,degset03*math.pi/180);
            }
            if (auxiliaryData[1]==50) {
                degset03=degset03-dif;
                simxSetJointTargetPosition(joint03,degset03*math.pi/180);

            }
            if (auxiliaryData[1]==54) {
                degset04=degset04+dif;
                simxSetJointTargetPosition(joint04,degset04*math.pi/180);
            }
            if (auxiliaryData[1]==52) {
                degset04=degset04-dif;
                simxSetJointTargetPosition(joint04,degset04*math.pi/180);
            }
            if (auxiliaryData[1]==49) {
                degset05=degset05+dif;
                simxSetJointTargetPosition(joint05,degset05*math.pi/180)
            }
            if (auxiliaryData[1]==51) {
                degset05=degset05-dif;
                simxSetJointTargetPosition(joint05,degset05*math.pi/180);
            }




            if  (auxiliaryData[1]==48){
                if (balance_contral==true){
                    balance_contral=false;
                else
                    balance_contral=true;
                }
            }
            if (balance_contral==true) {
                if (auxiliaryData[1]==2007) {
                    degset03=degset03+dif ;
                    simxSetJointTargetPosition(joint03,degset03*math.pi/180);
                }
                if (auxiliaryData[1]==2008) {
                    degset03=degset03-dif;
                    simxSetJointTargetPosition(joint03,degset03*math.pi/180);
                }
            }
        }
        message,auxiliaryData=simGetSimulatorMessage();
    }
}



