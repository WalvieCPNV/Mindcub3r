from pybricks.tools import wait, StopWatch, DataLog

from View.Center import Center
from View.Arm import Arm
from View.ColorSensor import colorSensor


class ControllerMotor:
    def __init__(self) -> None:
        pass
    def rotateCubeZ(self):
        pass
    def rotateCubeX(self):
        pass
    def turnFaceDownPrime(self):
        pass   
    def turnFaceDown(self):
        pass
    def scanCube(self):
        pass
"""
testCenter = Center()
testCenter.rotateCube(1)

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