class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiag = -1
        associatedArea = 0
        for x, y in dimensions:
            diag = (x **2 + y ** 2) ** 0.5
            area = x * y
            if diag > maxDiag or (diag == maxDiag and area > associatedArea):
                maxDiag = diag
                associatedArea = area
                
        
        return associatedArea