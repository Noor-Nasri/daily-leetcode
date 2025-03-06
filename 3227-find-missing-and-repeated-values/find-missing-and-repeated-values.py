class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values = {i for i in range(1, len(grid) * len(grid[0]) + 1)}
        result = []
        for lis in grid:
            for val in lis:
                if val not in values:
                    result.append(val)
                else:
                    values.remove(val)
        
        result.append(values.pop())
        return result
        