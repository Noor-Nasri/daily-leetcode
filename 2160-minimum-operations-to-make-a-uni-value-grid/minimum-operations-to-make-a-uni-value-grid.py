class Solution:
    def costForMinVal(self, value_counts, minVal, x):
        total = 0
        for val in value_counts:
            steps = (val - minVal) // x
            total += steps * value_counts[val]
        return total


    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # First, narrow it down to a list of possible uni-values, which will be spaced x apart
        # then, we just compute the first one and use a technique like sliding window / 2pointer
        # Every time we increase x, we need k more operations where k is the number of values <= previous val
        # But we also save j operations, where j is the number of values >= new val.

        value_counts = {}
        primaryVal = grid[0][0]
        minVal = 10**4 + 1
        maxVal = 0
        for row in grid:
            for val in row:
                if val in value_counts:
                    value_counts[val] += 1
                else:
                    value_counts[val] = 1
        
                # ensure all vals are spaced out with multiples of x
                if (val - primaryVal) % x != 0:
                    return -1

                minVal = min(minVal, val)
                maxVal = max(maxVal, val)
        
        curCost = self.costForMinVal(value_counts, minVal, x)
        bestCost = curCost
        numLeft = value_counts[minVal]
        numRight = len(grid) * len(grid[0]) - numLeft

        for newPivot in range(minVal + x, maxVal + 1, x):
            curCost += numLeft
            curCost -= numRight
            bestCost = min(bestCost, curCost)

            if newPivot in value_counts:
                numLeft += value_counts[newPivot]
                numRight -= value_counts[newPivot]


        return bestCost