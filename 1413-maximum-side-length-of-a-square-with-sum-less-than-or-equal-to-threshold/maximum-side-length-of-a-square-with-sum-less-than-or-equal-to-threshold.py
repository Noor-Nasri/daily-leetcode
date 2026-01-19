class Solution:
    # This one allows binary search because if we cant make size 2, we cannot make size > 2.
    # So we can just binary search on k, then verify in O(grid) sweep.
    def squareExists(self, prefixSums, sideLength):
        for row in range(sideLength - 1, self.nrow):
            for col in range(sideLength - 1, self.ncol):
                squareSum = prefixSums[row][col]
                if row - sideLength >= 0:
                    squareSum -= prefixSums[row - sideLength][col]
                if col - sideLength >= 0:
                    squareSum -= prefixSums[row][col - sideLength]

                if row - sideLength >= 0 and col - sideLength >= 0:
                    squareSum += prefixSums[row- sideLength][col - sideLength]

                if squareSum <= self.threshold:
                    return True

        return False


    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        self.threshold = threshold
        self.nrow, self.ncol = len(mat), len(mat[0])
        prefixSums = [ [mat[r][c] for c in range(self.ncol)] for r in range(self.nrow)]
        for row in range(self.nrow):
            for col in range(self.ncol):
                if row:
                    prefixSums[row][col] += prefixSums[row - 1][col]
                if col:
                    prefixSums[row][col] += prefixSums[row][col - 1]
                if row and col:
                    prefixSums[row][col] -= prefixSums[row - 1][col - 1]

        best = 0
        low = 1
        high = min(self.nrow, self.ncol)
        while low <= high:
            sideLength = (low + high) // 2
            if self.squareExists(prefixSums, sideLength):
                best = sideLength 
                low = sideLength + 1
            else:
                high = sideLength - 1

        return best
