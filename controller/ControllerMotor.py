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
        pass
    def turnFaceDownPrime(self):
        pass
    def turnFaceDown(self):
        pass
    def scanCube(self):
        pass

test = controllerMotor()
test.rotateCubeZ()

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