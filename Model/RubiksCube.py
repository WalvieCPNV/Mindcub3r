class rubiksCube:
    def __init__(self):
        #Creates a 3 by 3 by 6 array simulating the positions of the colors on a rubiks cube
        self.arrayColor = [[[0 for x in range(3)] for y in range(3)] for z in range(6)]
        self.algorythm = [0]
    def calculateAlgorythm(self):
        pass
    def getAlgorythm(self):
        pass
    def setColor(self, color):
        
        tableOrder = [
            [1, 1],
            [2, 1],
            [2, 2],
            [1, 2],
            [0, 2],
            [0, 1],
            [0, 0],
            [1, 0],
            [2, 0]
        ]

        for face in range(0, 6):
            for piece in range(0, len(tableOrder)):
                currentPiece = self.arrayColor[face][tableOrder[piece][0]][tableOrder[piece][1]]
                if (currentPiece == 0):
                    self.arrayColor[face][tableOrder[piece][0]][tableOrder[piece][1]] = color
                    return
