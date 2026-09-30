class Solution:
    # So the reason this is a hard is because a path may only become clearly non viable at the end
    # Eg: Take an open (, but all the way down to bottom/right is actually also open.
    # I want to say this question has 2 parts, first we precompute the values each cell can complete? 
    # Is there any other way? DP (row, col, depth) is too large.
    # Classic BFS would still need to track depth and its unclear if we prioritize in some way.

    # Can we just do DP actually, since depth can never be >100? Because the whole path can only be 200 anyways.
    # 100^3 should be fine. Probably a medium but a bit hard to read. 

    def checkPath(self, row, col, curDepth):
        if not (0 <= row < self.nrow and 0 <= col < self.ncol):
            return False
        
        curDepth += self.depthDiff[row][col]
        if curDepth < 0:
            return False

        uid = (row, col, curDepth)
        if uid in self.sols:
            return self.sols[uid]
        elif (row, col) == self.goal:
            return (curDepth == 0)

        self.sols[uid] = self.checkPath(row + 1, col, curDepth) or self.checkPath(row, col + 1, curDepth)
        return self.sols[uid]

    def hasValidPath(self, grid: list[list[str]]) -> bool:
        self.sols = {}
        self.nrow, self.ncol = len(grid), len(grid[0])
        self.goal = (self.nrow - 1, self.ncol - 1)
        self.depthDiff = [[e == "(" and 1 or -1 for e in row] for row in grid]
        return self.checkPath(0, 0, 0)