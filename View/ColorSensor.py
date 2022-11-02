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
        motorClass.rotate(self, 300, -500)
    def rotateToEdge(self):
        motorClass.rotate(self, 300, 175)
    def rotateToCorner(self, y):
        angle = 75*y
        motorClass.rotate(self, 300, angle)
    def resetPosition(self):
        motorClass.rotate(self, 300, 325) #325