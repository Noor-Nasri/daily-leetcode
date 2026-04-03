class Solution:
    # This seems like a simple DP: Each robot either shoots left or right
    # The trick is how you track previous bullets. All we need is: didlastRobotShootRight?
    # We can then determine the benifit of left vs right by getting the # of walls in ranges
    # So we can just do binary search.

    def indFirstWallGreaterEqPosition(self, pos):
        low, high, best = 0, len(self.walls) - 1, -1
        while low <= high:
            mid = (low + high)//2
            if self.walls[mid] >= pos:
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        return best

    def indLastWallSmallerEqPosition(self, pos):
        low, high, best = 0, len(self.walls) - 1, -1
        while low <= high:
            mid = (low + high)//2
            if self.walls[mid] <= pos:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best

    def numWallsInRangeInclusive(self, left, right):
        if left > right:
            return 0
        indL = self.indFirstWallGreaterEqPosition(left)
        indR = self.indLastWallSmallerEqPosition(right)
        if indL == -1 or indR == -1:
            return 0
        
        return indR - indL + 1
    
    def solveMaxWalls(self, robotInd, incomingBullet):
        uid = (robotInd, incomingBullet)
        if robotInd == len(self.robots):
            return 0
        elif uid in self.sols:
            return self.sols[uid]
        
        pos, dist = self.robots[robotInd]
        leftCutoff, rightCutoff = pos - dist, pos + dist
        if robotInd:
            prevPos, prevDist = self.robots[robotInd - 1]
            if incomingBullet:
                prevPos = min(pos, prevPos + prevDist)
            leftCutoff = max(leftCutoff, prevPos + 1)
            
        if robotInd < len(self.robots) - 1:
            nextPos, _ = self.robots[robotInd + 1]
            rightCutoff = min(rightCutoff, nextPos - 1)
        
        op1 = self.numWallsInRangeInclusive(leftCutoff, pos) + self.solveMaxWalls(robotInd + 1, False)
        op2 = self.numWallsInRangeInclusive(pos, rightCutoff) + self.solveMaxWalls(robotInd + 1, True)
        self.sols[uid] = max(op1, op2)
        return self.sols[uid]

    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        self.robots = sorted([(robots[i], distance[i]) for i in range(len(robots))])
        self.walls = sorted(walls)
        self.sols = {}
        return self.solveMaxWalls(0, False)