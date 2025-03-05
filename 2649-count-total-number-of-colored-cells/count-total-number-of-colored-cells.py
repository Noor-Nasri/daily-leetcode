class Solution:
    def coloredCells(self, n: int) -> int:
        # middle row: 1 + 2 *(n-1) = 2n - 1
        # other rows total: 2 * (1 + 3 + ... + (2n - 3))
        # = 2 * (1 + 2n - 3)/2 * [n - 1] = (2n - 2) * (n - 1)
        # therefore total is 2n - 1 + 2 * (n - 1)^2 = 2n^2 - 2n + 1
        return 1 + 2*(n**2 - n) 