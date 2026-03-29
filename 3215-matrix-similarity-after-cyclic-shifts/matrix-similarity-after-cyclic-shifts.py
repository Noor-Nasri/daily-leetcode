class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        nrow, ncol = len(mat), len(mat[0])
        for row in range(nrow):
            shift = ((row % 2) * 2 - 1) * k
            for col in range(ncol):
                newCol = (col + shift) % ncol
                if mat[row][col] != mat[row][newCol]:
                    return False
        
        return True
                