class Solution:
    # Basic 2d rolling sums but its been a while since I used this. 
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        finalArr = [[0 for i in range(n)] for j in range(n)]
        for row1, col1, row2, col2 in queries:
            finalArr[row1][col1] += 1
            if row2 + 1 < n:
                finalArr[row2 + 1][col1] -= 1
            if col2 + 1 < n:
                finalArr[row1][col2 + 1] -= 1
            
            if row2 + 1 < n and col2 + 1 < n:
                finalArr[row2 + 1][col2 + 1] += 1

        for row in range(n):
            for col in range(n):
                if row:
                    finalArr[row][col] += finalArr[row - 1][col]
                if col:
                    finalArr[row][col] += finalArr[row][col - 1]
                if row and col:
                    finalArr[row][col] -= finalArr[row - 1][col - 1]
        
        return finalArr



