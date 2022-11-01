from View import Motor

class Arm(Motor.Motor):
    def __init__(self):
        Motor.Motor.__init__(self, Port.C)
    def rotateCubeXPrime(self):
        pass
    def lockCube(self):
        pass
    def releaseCube(self):
        pass

