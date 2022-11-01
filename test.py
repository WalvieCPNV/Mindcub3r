
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import uasyncio


# Create your objects here.
ev3 = EV3Brick()

# Initialize the motors.
# cube_motor = Motor(Port.B)

#motorColorSensor = Motor(Port.A)
#motorCenter = Motor(Port.B)
#colorSensor = ColorSensor(Port.S1)


class ColorSensor:
    def __init__(self):
        self.angle = 0
    #def scanColor(self):
        #colorsensor.color()
    async def rotateToCenter(self):
        motorColorSensor.run_target(300, -500, then=Stop.HOLD, wait=True)
    async def rotateToEdge(self):
        motorColorSensor.run_target(300, -340, then=Stop.HOLD, wait=True)
    async def rotateToCorner(self):
        motorColorSensor.run_target(300, -320, then=Stop.HOLD, wait=True)
    async def resetPosition(self):
        motorColorSensor.run_target(300, 0, then=Stop.HOLD, wait=True)

class Center:
    def __init__(self):
        self.angle = 0
    async def RotateCube(self, y):
        #motorCenter.run_angle(300, y, then=Stop.HOLD, wait=True)
        pass



ev3.speaker.beep()
motorColorSensor.run_angle(300, 500, then=Stop.HOLD, wait=True)
"""""
test = ColorSensor()
test2 = Center()

test.rotateToCenter()
#test.scanColor()

test.rotateToEdge()
#test.scanColor()

test2.RotateCube(135)

test.rotateToCorner()
#test.scanColor()

test2.RotateCube(135)

test.rotateToEdge()

test2.RotateCube(135)
test2.RotateCube(135)

test.resetPosition()

#test.scanColor()


uasyncio.run(test.rotateToCenter())
uasyncio.run(test2.RotateCube(1000))


#motorColorSensor.run_angle(300, 340, then=Stop.HOLD, wait=True)

"""""






