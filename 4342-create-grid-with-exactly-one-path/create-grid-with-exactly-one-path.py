class Solution:
    # lol what is this question. Just make a grid of all # except top right edge
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#' for col in range(n)] for row in range(m)]
        for col in range(n):
            grid[0][col] = '.'
        
        for row in range(m):
            grid[row][-1] = '.'
        
        return ["".join(e) for e in grid]