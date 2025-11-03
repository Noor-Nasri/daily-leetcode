class Solution:
    # Ignoring the time constrainst, we can choose to pop each time we get a consecutive one
    # So, if we have a balloon we need to pop but can't due to time, we need more time
    # We can do a clean binary search but I think one pass should work here. 
    # For each group of same colours, we pop all but the one that needs most time

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        minSolveTime = 0
        
        curColor = -1
        biggestConstraint = 0
        chainCost = 0

        for i in range(len(colors)):
            col, time = colors[i], neededTime[i]

            if col == curColor:
                biggestConstraint = max(biggestConstraint, time)
                chainCost += time
                    
            else:
                minSolveTime += chainCost - biggestConstraint
                biggestConstraint = time
                chainCost = time

            curColor = col
        

        minSolveTime += chainCost - biggestConstraint

        return minSolveTime
        