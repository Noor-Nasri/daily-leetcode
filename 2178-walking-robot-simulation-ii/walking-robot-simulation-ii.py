# This seems like a trivial tracker, but we can't actually simulate all steps
# Instead, we can actually reduce this to just the perimeter cells, we simply go in circle around them
# So all we need to track is the ind around the perimeter, and we can compute position on demand!

# Can any position be tied to multiple directions? NO! If you are on the last point of the line,
# Then you are still facing along the line. If you had rotated, you'd already be moved.

class Robot:
    def __init__(self, width: int, height: int):
        self.lastX, self.lastY = width - 1, height - 1
        self.curInd = 0
        self.curPos = [0, 0]
        self.curDir = "East"
        self.totalPerimeter = 2 * (height + width - 2)
        
        self.bottomRightInd = width - 1
        self.topRightInd = width + height - 2
        self.topLeftInd = 2*width + height - 3

    def step(self, num: int) -> None:
        self.curInd = (self.curInd + num) % self.totalPerimeter
        if 1 <= self.curInd <= self.bottomRightInd:
            self.curDir = "East"
            self.curPos = [self.curInd, 0]

        elif self.bottomRightInd + 1 <= self.curInd <= self.topRightInd:
            distAlongLine = self.curInd - self.bottomRightInd
            self.curPos = [self.lastX, distAlongLine]
            self.curDir = "North"
        
        elif self.topRightInd + 1 <= self.curInd <= self.topLeftInd:
            distAlongLine = self.curInd - self.topRightInd
            self.curPos = [self.lastX - distAlongLine, self.lastY]
            self.curDir = "West"
        
        else:
            distAlongLine = (self.curInd or self.totalPerimeter) - self.topLeftInd
            self.curPos = [0, self.lastY - distAlongLine]
            self.curDir = "South"

    def getPos(self) -> List[int]:
        return self.curPos
        

    def getDir(self) -> str:
        return self.curDir

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()