class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Idea: for each row, generate which flips are needed to make all 0s (and 1s are the composite)
        # If two rows have a match or are opposites, they can both be active at once. 
        # If not, they'll never match up. For ex Row 0 has 001 while row 1 has 011. 
        
        # Thus: Just need largest number of matches
        matches = {}
        best = 0

        for row in matrix: 
            if row[0]: # Store keys with first element as 1
                vals = tuple(row)
            else:
                vals = tuple([1 - e for e in row])


            if not vals in matches:
                matches[vals] = 0

            matches[vals] += 1
            if matches[vals] > best:
                best = matches[vals] 

        return best
        
        