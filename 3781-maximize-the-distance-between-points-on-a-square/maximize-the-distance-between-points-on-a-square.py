class Solution:
    # I see a few quick ideas here:
    # 1: We can iterate on the min Dist with binary search, then need to verify the dist in O(n)
    # 2: If we know the distance, then including a point means we go down the line until val > inc + dist
    #      - Because its a cycling on a perimeter, going to an adjacent line is always longer than finishing your line
    #      - So we can treat the current and next line as one long line.
    # 3: Combining (1, 2) means we can do a DP solve in O(N) by flipping it: given minDist, solve max elements!

    # Problem: If we take point in line 1, we may have region within line 3 that cant be taken.
    # This felt tricky but actually: if side >= minDist, then thats not relevant!
    # Doing it on paper:  If side < minDist, then we actually never reach p = 4 >= k
    #   Say dist=10.1 and side=10. Place p1 at (0, 5). Then p2 is (5.1, 0). Then (10, 5.2). Can't place 4th!
    
    # Okay .. what about line 4? We need to exclude nodes at the end based on init
    #   but (ind_st, ind_cur) is too expensive to DP. Maybe we do [ind] -> (max #, last_taken_ind)

    # Conclusion: BS on minDist, then solve DP table in O(N), then O(N) sweep to check maxCount(startInd) >= k

    def remapPoints(self, points, sideLength):
        # Since we work our way around and don't need to jump across parallel lines, 
        # we can stretch the perimeter into a single line.
        
        stretchedPoints = []
        for x, y in points:
            if x == 0 or y == sideLength: # Going up then going right
                dist = x + y
            else: # Going down then left
                dist = sideLength*4 - (x + y)

            stretchedPoints.append(dist)
        
        return sorted(stretchedPoints)
    
    def solvePointers(self, stretchedPoints, minDist):
        # Returns [ first ind of val >= curVal + minDist]
        nextPoints = []
        curPointer = 1
        for ind in range(len(stretchedPoints)):
            val = stretchedPoints[ind]
            curPointer = max(curPointer, ind + 1)
            while curPointer < len(stretchedPoints) and stretchedPoints[curPointer] < val + minDist:
                curPointer += 1
            
            nextPoints.append(curPointer)
        
        return nextPoints

    def solveMaxPoints(self, sols, stretchedPoints, nextPoints, curInd):
        # Returns (max points, smallest final ind needed for those points)
        if curInd in sols:
            return sols[curInd]
        
        options = []
        if curInd < len(stretchedPoints) - 1:
            options.append(self.solveMaxPoints(sols, stretchedPoints, nextPoints, curInd + 1))
        
        if nextPoints[curInd] < len(stretchedPoints):
            maxVal, earliestInd = self.solveMaxPoints(sols, stretchedPoints, nextPoints, nextPoints[curInd])
            options.append((maxVal + 1, earliestInd))
        else:
            options.append((1, curInd))

        bestOption = options[0]
        if len(options) == 2:
            if options[1][0] > options[0][0] or (options[1][0] == options[0][0] and options[1][1] < options[0][1]):
                bestOption = options[1]
        
        sols[curInd] = bestOption
        return sols[curInd]
    
    def realPointFromStretched(self, sideLength, p):
        if p <= sideLength:
            return (0, p)
        elif p <= 2*sideLength:
            return (p - sideLength, sideLength)
        elif p <= 3*sideLength:
            return (sideLength, 3*sideLength - p)
        else:
            return (4*sideLength - p, 0)

    def realDistBetweenStretched(self, sideLength, p1, p2):
        x1, y1 = self.realPointFromStretched(sideLength, p1)
        x2, y2 = self.realPointFromStretched(sideLength, p2)
        dist = abs(x1 - x2) + abs(y1 - y2)
        #print(f"Points {p1} and {p2} are at positions {(x1, y1)} and {(x2, y2)}, which are {dist} apart")
        return dist

    def verifyMinDist(self, sideLength, stretchedPoints, k, minDist):
        #print(f"====== checking minDist ={minDist} ======")
        nextPoints = self.solvePointers(stretchedPoints, minDist)
        
        #print("Next pointers:", nextPoints)
        sols = {}
        self.solveMaxPoints(sols, stretchedPoints, nextPoints, 0)
        #for i in range(len(stretchedPoints)):
            #print(f"Point {i} is at {self.realPointFromStretched(sideLength, stretchedPoints[i])}, and gets {sols[i]}")

        for startInd in range(len(stretchedPoints) - 1):
            maxPoints, lastInd = sols[startInd]
            if maxPoints > k:
                return True
            elif maxPoints < k:
                return False
            
            startPos = stretchedPoints[startInd]
            endPos = stretchedPoints[lastInd]
            if maxPoints == k and self.realDistBetweenStretched(sideLength, startPos, endPos) >= minDist:
                return True
        
        return False

    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        stretchedPoints = self.remapPoints(points, side)
        #print(stretchedPoints)
        low = 1 # since points are unique, 1 is always an option
        high = side # Once minDist > side, we can have at most 3, but k <= 3.
        best = low

        while low <= high:
            mid = (low + high) // 2
            if self.verifyMinDist(side, stretchedPoints, k, mid):
                #print("Yes! Will look even higher")
                best = mid
                low = mid + 1
            else:
                #print("No :(. Will look lower")
                high = mid - 1
        
        return best
