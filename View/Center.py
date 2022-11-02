from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

from View.Motor import MotorClass

class Center(MotorClass):
    def __init__(self):
        MotorClass.__init__(self, motorCenter)
    def rotateCube(self, y):
        angle = 270*y
        MotorClass.rotate(self, 300, angle)
