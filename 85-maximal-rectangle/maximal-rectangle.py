class Solution:
    # At each point, we can compute maximal rect area that ends there
    # We would iterate across each col, and get the number of rows via binary search. O(n^3logn)
    # Other ideas could be to group the 1s first, then look for largest clump in each island?

    # Or can we do BS on the number of 1s we are looking for?
    # For example: if we wanted 100 1s, we would find multiples of 100 and try them all rectangles.
    # This would be O(n^2log(n^2)*(maxFactors)). Definitely faster than other solution.
    # GAAH, I wasted time on this but it wont work because sometimes you can make a 2x2 but not a 3x1 .. 
    # Just gonna do the basic search and hope it doesnt tle

    def getLargestAreaGivenBase(self, oneSums, row_start, row_end, col_end):
        # use BS to get min col where the whole rect is filled
        low = 0
        high = col_end
        best = col_end

        while low <= high:
            col_start = (low + high) // 2

            numOnes = oneSums[row_end][col_end]
            if row_start:
                numOnes -= oneSums[row_start - 1][col_end]
            if col_start:
                numOnes -= oneSums[row_end][col_start - 1]
            if row_start and col_start:
                numOnes += oneSums[row_start - 1][col_start - 1]
            
            expectedOnes = (row_end - row_start + 1) * (col_end - col_start + 1)
            if numOnes == expectedOnes:
                best = col_start
                high = col_start - 1
            else:
                low = col_start + 1

        return (row_end - row_start + 1) * (col_end - best + 1)
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # First compute prefix sums so we can easily verify if a rect is all 1s
        oneSums = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        best = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row:
                    oneSums[row][col] += oneSums[row - 1][col]
                if col:
                    oneSums[row][col] += oneSums[row][col - 1]
                if row and col:
                    oneSums[row][col] -= oneSums[row - 1][col - 1]

                if matrix[row][col] == "0":
                    continue

                oneSums[row][col] += 1
                for rowStart in range(row, -1, -1):
                    if matrix[rowStart][col] == "0":
                        break

                    numOnes = self.getLargestAreaGivenBase(oneSums, rowStart, row, col)
                    best = max(best, numOnes)


        return best

        
