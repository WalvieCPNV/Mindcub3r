from pybricks.tools import wait, StopWatch, DataLog
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

from View.Motor import MotorClass

class Arm(MotorClass):
    def __init__(self):
        motorArm = Motor(Port.C)
        MotorClass.__init__(self, motorArm)
    def rotateCubeXPrime(self):
        MotorClass.rotate(self, 200, 200)
        MotorClass.rotate(self, 200, -100)
    def lockCube(self):
        MotorClass.rotate(self, 200, 100)
    def releaseCube(self):
        MotorClass.rotate(self, 200, -100)

