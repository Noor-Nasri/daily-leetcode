class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n_row, n_col = len(mat), len(mat[0])
        remainingInRows = [n_col for i in range(n_row)]
        remainingInCols = [n_row for i in range(n_col)]
        
        locations = {}
        for row in range(n_row):
            for col in range(n_col):
                locations[mat[row][col]] = (row, col)
        
        for ind in range(len(arr)):
            row, col = locations[arr[ind]]
            remainingInRows[row] -= 1
            remainingInCols[col] -= 1

            if remainingInRows[row] == 0 or remainingInCols[col] == 0:
                return ind
        
        return len(arr)
