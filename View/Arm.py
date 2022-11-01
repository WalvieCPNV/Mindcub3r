from View.Motor import Motor

class Arm(Motor):
    def __init__(self):
        Motor.__init__(self, Port.C)
    def rotateCubeXPrime(self):
        pass
    def lockCube(self):
        pass
    def releaseCube(self):
        pass

