class Solution:
    def solve(self, row, col):
        if (row, col) in self.sols:
            return self.sols[(row, col)]

        options = [0]
        for delta_r, delta_c in self.movements:
            new_row, new_col = row + delta_r, col + delta_c
            if not (0 <= new_row < self.n_rows and 0 <= new_col < self.n_cols):
                continue
            if self.matrix[new_row][new_col] > self.matrix[row][col]:
                options.append(1 + self.solve(new_row, new_col))

        self.sols[(row, col)] = max(options)
        return self.sols[(row, col)]


    def maxMoves(self, grid: List[List[int]]) -> int:
        self.matrix = grid
        self.sols = {}
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        self.movements = ((-1, 1), (0, 1), (1, 1))

        best = 0
        for row in range(self.n_rows):
            best = max(best, self.solve(row, 0))

        return best

        