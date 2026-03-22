class Solution:
    def rotateMat(self, mat):
        # To rotate, we can tilt our head to the left and see where the new rows come from
        # The first column, read from down to top, becomes the first row. And so on.
        newMat = []
        for col in range(len(mat[0])):
            newRow = []
            for row in range(len(mat) - 1, -1, -1):
                newRow.append(mat[row][col])
            newMat.append(newRow)
        return newMat

    def checkEq(self, mat1, mat2):
        for row in range(len(mat1)):
            for col in range(len(mat1[0])):
                if mat1[row][col] != mat2[row][col]:
                    return False
        return True 

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            mat = self.rotateMat(mat)
            if self.checkEq(mat, target):
                return True
        
        return False