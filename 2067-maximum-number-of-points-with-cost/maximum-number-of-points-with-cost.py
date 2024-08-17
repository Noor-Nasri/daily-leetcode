class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # This was really tricky to solve in O(rc) instead of O(r*c^2)
        # Bringing it to O(r*c^2) means solving with a layer of DP, going one row at a time
        # Then at each row, instead of considering every option for each column,
        # That computation can be solved in O(n) by splitting the left and right choices

        ncols = len(points[0])
        curValues = points[0]
        for row in range(1, len(points)):
            bestOptionFromLeft = [curValues[0]]
            for col in range(1, ncols):
                bestOption = max(curValues[col], bestOptionFromLeft[-1] - 1)
                bestOptionFromLeft.append(bestOption)
            
            bestOptionFromRight = [curValues[-1]]
            for col in range(ncols - 2, -1, -1):
                bestOption = max(curValues[col], bestOptionFromRight[-1] - 1)
                bestOptionFromRight.append(bestOption)
            bestOptionFromRight = bestOptionFromRight[::-1]

            nextValues = []
            for col in range(ncols):
                bonus = max(bestOptionFromLeft[col], bestOptionFromRight[col])
                nextValues.append(points[row][col] + bonus)
            curValues = nextValues
        
        return max(curValues)



        