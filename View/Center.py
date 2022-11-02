from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

from View.Motor import motorClass

class center(motorClass):
    def __init__(self):
        motorCenter = Motor(Port.B)
        motorClass.__init__(self, motorCenter)
    def rotateCube(self, y):
        angle = 270*y
        motorClass.rotate(self, 300, angle)
        motorClass
