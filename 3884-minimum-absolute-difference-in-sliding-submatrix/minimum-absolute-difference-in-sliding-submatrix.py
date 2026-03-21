class Solution:
    # m and n are <= 30, cant we just do brute force computation?
    # We can setup a sliding window but it seems complicated. Just make a set of numbers then loop on it.

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        solution = []

        for row_start in range(len(grid) - k + 1):
            nextRow = []
            for col_start in range(len(grid[0]) - k + 1):
                values = set()
                for offsetx in range(k):
                    for offsety in range(k):
                        values.add(grid[row_start + offsetx][col_start + offsety])
                
                items = sorted(list(values))
                if len(items) == 1:
                    nextRow.append(0)
                else:
                    minDiff = 10**6
                    for ind in range(len(items) - 1):
                        minDiff = min(minDiff, items[ind + 1] - items[ind])
                    nextRow.append(minDiff)
            
            solution.append(nextRow)

        return solution    