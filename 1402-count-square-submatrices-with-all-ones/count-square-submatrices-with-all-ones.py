class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        sums = [] # gives sum of elements from (0,0) to that corner of rect
        n_row, n_col = len(matrix), len(matrix[0])
        for row in range(n_row):
            sums.append([])
            total = 0
            for col in range(n_col):
                total += matrix[row][col]
                sums[-1].append(total)
                if row > 0:
                    sums[-1][-1] += sums[row - 1][col]
        
        #print(sums)
        
        # need to check for valid number of (corner, corner)
        # This is 300^4 unfortunately. Can instead do start x size, which is 300^3
        # Can optimize by adding all subsquares  as needed
        found = 0
        for row_start in range(n_row):
            possible_h = n_row - row_start

            for col_start in range(n_col):
                possible_w = n_col - col_start
            
                for side_len in range(min(possible_h, possible_w)-1, -1, -1):
                    # side_len is number of elements-1 in each side of square
                    square_total = sums[row_start + side_len][col_start + side_len]
                    #print("Looking at", row_start, col_start, side_len, square_total)

                    if row_start:
                        square_total -= sums[row_start - 1][col_start + side_len]
                        #print("remove above", sums[row_start - 1][col_start + side_len] )
                    
                    if col_start:
                        square_total -= sums[row_start + side_len][col_start - 1]
                        #print("remove left", sums[row_start + side_len][col_start - 1])
                    
                    if row_start and col_start: # we double removed
                        square_total += sums[row_start - 1][col_start - 1]
                        #print("add back extra",sums[row_start - 1][col_start - 1] )
                    
                    #print("gives us", square_total)

                    if square_total == (side_len+1)*(side_len+1):
                        #everything in this side length is a valud submattrix for this starting index
                        found += side_len+1
                        break

        return found
        