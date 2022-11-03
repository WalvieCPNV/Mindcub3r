from pybricks.tools import wait, StopWatch, DataLog

from View.Center import center
from View.Arm import arm
from View.ColorSensor import colorSensor


MotorArm = arm()
MotorSensor = colorSensor()
MotorCenter = center()


class controllerMotor:
    def __init__(self):
        pass
    def rotateCubeZ(self):
        MotorCenter.rotateCube(1)
        wait(200)
        MotorArm.rotateCubeXPrime()
        wait(200)
        MotorArm.releaseCube()
        wait(200)
        MotorCenter.rotateCube(-1)
    def rotateCubeX(self):
        MotorCenter.rotateCube(2)
        wait(200)
        MotorArm.rotateCubeXPrime()
        wait(200)
        MotorArm.releaseCube()
        wait(200)
        MotorCenter.rotateCube(-2)
    def turnFaceDownPrime(self):
        MotorArm.lockCube()
        wait(200)
        MotorCenter.rotateCube(1)
        wait(200)
        MotorArm.releaseCube()
    def turnFaceDown(self):
        MotorArm.lockCube()
        wait(200)
        MotorCenter.rotateCube(-1)
        wait(200)
        MotorArm.releaseCube()
    def scanOneFace(self):

        #avance au millieu et scan la couleur
        MotorSensor.rotateToCenter()
        print(MotorSensor.scanColor())
        wait(200)

        #se positionne sur le coter
        MotorSensor.rotateToCornerTarget()
        wait(200)

        #scan la couleur et bouge 8x
        for x in range(2,10):
            MotorCenter.rotateCube(0.5)
            print(MotorSensor.scanColor())
            wait(100)

            """
            #le 1er vas bcp plus loin jsp pk
            if(x%2 == 0):
                MotorSensor.rotateToCornerTarget()    
                print("1")
            else:
                MotorSensor.rotateToEdge()
                print("2")
            wait(200)
            """
        #remet le sensor en position de depart
        MotorSensor.resetPosition()
    def scanCube(self):
        pass

test = controllerMotor()
test.scanOneFace()
#MotorSensor.rotateToCorner()
#MotorCenter.rotateCube(1)
#MotorSensor.rotateToEdge()





"""
for x in range(0, 10):
    testCenter = center()
    testCenter.rotateCube(1)
    wait(1000)

testMotorSensor = colorSensor()


for x in range(0, 2):
    testMotorSensor.rotateToCenter()
    wait(1000)
    testMotorSensor.rotateToEdge()
    wait(1000)
    testMotorSensor.resetPosition()
    wait(1000)


testMotorArm = Arm()
for x in range(0,1):
    testMotorArm.rotateCubeXPrime()
    wait(1000)
    testMotorArm.releaseCube()
    wait(1)
"""