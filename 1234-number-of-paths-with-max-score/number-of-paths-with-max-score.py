class Solution:
    # So it immediately seems like DP: (row, col) -> maxScore, count
    # At each point, there are 3 options, then add up the counts
    # This seems more like medium .. am I missing something? Just modulo and done?

    def solvePaths(self, row, col):
        uid = (row, col)
        val = self.grid[row][col]
        if uid in self.sols:
            return self.sols[uid]
        elif row < 0 or col < 0 or val == "X":
            return [0, 0]
        elif val == "E":
            return [0, 1]

        options = [
            self.solvePaths(row - 1, col),
            self.solvePaths(row, col - 1),
            self.solvePaths(row - 1, col - 1)
        ]

        trueMax = max(options[0][0], options[1][0], options[2][0])
        trueCount = sum([
            e[0] == trueMax and e[1] or 0 for e in options
        ]) % (10**9 + 7)

        if trueCount:
            trueMax += val
            
        self.sols[uid] = [trueMax, trueCount]
        return self.sols[uid]

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        self.nrow, self.ncol = len(board), len(board[0])
        self.grid = [[(el.isdigit() and int(el) or el) for el in row] for row in board]
        self.grid[-1][-1] = 0
        self.sols = {}
        return self.solvePaths(self.nrow - 1, self.ncol - 1)