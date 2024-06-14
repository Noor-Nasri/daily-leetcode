class Solution:
    def floodfill(self, realGrid, curX, curY, value):
        if (curX < 0 or curX >= len(realGrid) or curY < 0 or curY >= len(realGrid)):
            return
        
        if realGrid[curX][curY] == 1 or realGrid[curX][curY] == value:
            return
        

        realGrid[curX][curY] = value
        self.floodfill(realGrid, curX+1, curY, value)
        self.floodfill(realGrid, curX-1, curY, value)
        self.floodfill(realGrid, curX, curY+1, value)
        self.floodfill(realGrid, curX, curY-1, value)

        # can also floodfill diagonally in edge cases
        if (curX % 2 == 0 and curY % 2 == 1):
            # Lower left, can always go up then left
            # To reach here, it is either \ or space
            # If other side is /, it returns.
            # Same logic all the way down ..
            self.floodfill(realGrid, curX-1, curY-1, value)
            self.floodfill(realGrid, curX+1, curY+1, value)

        elif (curX % 2 == 1 and curY % 2 == 0):
            self.floodfill(realGrid, curX-1, curY-1, value)
            self.floodfill(realGrid, curX+1, curY+1, value)
        
        elif (curX % 2 == 0 and curY % 2 == 0):
            self.floodfill(realGrid, curX-1, curY+1, value)
            self.floodfill(realGrid, curX+1, curY-1, value)
        
        elif (curX % 2 == 1 and curY % 2 == 1):
            self.floodfill(realGrid, curX-1, curY+1, value)
            self.floodfill(realGrid, curX+1, curY-1, value)
        
            





    def regionsBySlashes(self, grid: List[str]) -> int:
        # This question seemed very difficult until I realized
        # just treat each 1x1 as a 2x2. The dash simply connects two corners
        # At the end, simple floodfill to see what is connected

        n = len(grid)
        realGrid = [[0 for i in range(n*2)] for j in range(n*2)]

        for row in range(n):
            for col in range(n):
                if grid[row][col] == " ": continue
                if grid[row][col] == "/":
                    realGrid[row*2 + 1][col*2] = 1
                    realGrid[row*2][col*2 + 1] = 1
                else: # \ arrow
                    realGrid[row*2][col*2] = 1
                    realGrid[row*2 + 1][col*2 + 1] = 1

        regionValue = 2
        for row in range(n*2):
            for col in range(n*2):
                if realGrid[row][col] == 0:
                    self.floodfill(realGrid, row, col, regionValue)
                    regionValue+=1

        return regionValue - 2