class Solution:
    # Okay, since we can move all the columns we can just make the rect start at col 0
    # So what we really need is to figure out the starting row, and then how big we can go
    # Lets say we've picked a row (m options): What is the maximal length?
    # We need to know how many columns in row x are 1. That is our max.
    # What about 2nd row? We need to know how many columns have row x AND row x+1 as 1.

    # So what we need to precompute is: For every row, how many 1s, then how many have a 1 on top, etc.
    # This can be done in O(m * n). For each row, we sweep and account for the number of 1s.
    # By updating one array then doing a sweep, we then know exactly how long any rectangle can be.

    # With this, we can simply sweep for the lower left corner. Per row, we increase the col until 0 area.
    # We can optimize this with BS, but there is no point since we do O(m*n) above. So we do the same.
    # We can actually merge this into one sweep as we compute each row


    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        maxArea = 0
        numOnesChained = [0 for i in range(len(matrix[0]))]

        for row in range(len(matrix)):
            numLinesAvailableGivenLength = {}
            # [y] = number of lines we can put together that have a stack of 1s >= y

            for col in range(len(matrix[row])):
                if matrix[row][col]:
                    numOnesChained[col] += 1
                else:
                    numOnesChained[col] = 0
                
                length = numOnesChained[col]
                numLinesAvailableGivenLength[length] = numLinesAvailableGivenLength.get(length, 0) + 1
            
            numLinesAvail = 0
            lengthCheckpoints = sorted(list(numLinesAvailableGivenLength.keys()), reverse = True)
            for possibleHeight in lengthCheckpoints:
                numLinesAvail += numLinesAvailableGivenLength[possibleHeight]
                area = possibleHeight*numLinesAvail
                maxArea = max(maxArea, area)

        return int(maxArea)