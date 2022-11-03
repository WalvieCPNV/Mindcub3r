from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

from Model import RubiksCube
from View.Motor import motorClass

class colorSensor(motorClass):
    def __init__(self):
        motorSensor = Motor(Port.A)
        self.colorSensor = ColorSensor(Port.S1)
        motorClass.__init__(self, motorSensor)
    def scanColor(self):
        currentColor = self.colorSensor.rgb()
        colorR, colorG, colorB = currentColor

        redColorValue = {
            72 : "WHITE",
            9 : "BLUE",
            44 : "RED",
            10 : "GREEN",
            55 : "ORANGE",
            68 : "YELLOW"
        }

        greenColorValue = {
            89 : "WHITE",
            27 : "BLUE",
            67 : "RED",
            44 : "GREEN",
            73 : "ORANGE",
            81 : "YELLOW"
        }
             
        actualColor = redColorValue[min(redColorValue, key = lambda x: abs(x - colorR))]

        if actualColor == "GREEN" or actualColor == "BLUE":
            actualColor = greenColorValue[min(greenColorValue, key = lambda x: abs(x - colorG))]
        """
        using the moyu cube:
        
        WHITE: (75, 89, 100)
        BLUE: (9, 27, 69)
        RED: (44, 67, 82)
        GREEN: (10, 44, 95)
        ORANGE: (51, 73, 100)
        YELLOW:  (66, 81, 100)
        """
        print(colorR, colorG, colorB, actualColor)
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