from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

from Model import RubiksCube
from View.Motor import motorClass

class colorSensor(motorClass):
    def __init__(self):
        motorSensor = Motor(Port.A)
        #self.colorSensor = Sensor(Port.S1)
        motorClass.__init__(self, motorSensor)
    def scanColor(self):
        pass
    def rotateToCenter(self):
        motorClass.rotateTarget(self, 300, -550)
    def rotateToEdge(self):
        motorClass.rotateTarget(self, 300, -380)
    def rotateToCorner(self):
        motorClass.rotate(self, 300, 500)
    def rotateToCornerTarget(self):
        motorClass.rotateTarget(self, 300, -420)
    def resetPosition(self):
        motorClass.rotateTarget(self, 300, 0) #325