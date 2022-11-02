from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

from Model import RubiksCube
from View.Motor import MotorClass

class colorSensor(MotorClass):
    def __init__(self):
        motorSensor = Motor(Port.A)
        #self.colorSensor = Sensor(Port.S1)
        MotorClass.__init__(self, motorSensor)
    def scanColor(self):
        pass
    def rotateToCenter(self):
        MotorClass.rotate(self, 300, -500)
    def rotateToEdge(self):
        MotorClass.rotate(self, 300, 175)
    def rotateToCorner(self):
        MotorClass.rotate(self, 300, 20)
    def resetPosition(self):
        MotorClass.rotate(self, 300, 325)