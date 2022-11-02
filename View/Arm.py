from pybricks.tools import wait, StopWatch, DataLog
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

from View.Motor import motorClass

class arm(motorClass):
    def __init__(self):
        motorArm = Motor(Port.C)
        motorClass.__init__(self, motorArm)
    def rotateCubeXPrime(self):
        motorClass.rotate(self, 200, 200)
        motorClass.rotate(self, 200, -100)
    def lockCube(self):
        motorClass.rotate(self, 200, 100)
    def releaseCube(self):
        motorClass.rotate(self, 200, -100)

