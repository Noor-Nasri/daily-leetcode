class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # Only one real decision: At which point do we switch rows
        # Next robot has two options:
        #   - Collect remaining in row, meaning ignore bottom row completely
        #   - Switch row right away, meaning collect bottom row until our switch

        sumRows = [[0], [0]]
        for ind in range(len(grid[0])):
            sumRows[0].append(sumRows[0][-1] + grid[0][ind])
            sumRows[1].append(sumRows[1][-1] + grid[1][ind])
        
        minRobot2 = float("inf")
        for ind in range(len(grid[0])):
            op1 = sumRows[0][-1] - sumRows[0][ind + 1]
            op2 = sumRows[1][ind]
            minRobot2 = min(minRobot2, max(op1, op2))
        
        return minRobot2