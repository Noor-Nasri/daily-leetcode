class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        solution = []
        m = len(matrix)
        n = len(matrix[0])

        num_spirals = 0
        while len(solution) < n*m:
            topLeft = (num_spirals, num_spirals)
            bottomRight = (n - 1 - num_spirals, m - 1 - num_spirals)

            # Go right
            for x_new in range(topLeft[0], bottomRight[0] + 1):
                solution.append(matrix[num_spirals][x_new])
            
            if topLeft[1] == bottomRight[1]:
                return solution # Finished last row
            
            # Go down
            for y_new in range(topLeft[1] + 1, bottomRight[1] + 1):
                solution.append(matrix[y_new][bottomRight[0]])

            if topLeft[0] == bottomRight[0]:
                return solution # Finished last col


            # Go left
            for x_new in range(bottomRight[0] - 1, topLeft[0] - 1, -1):
                solution.append(matrix[bottomRight[1]][x_new])

            # Go up
            for y_new in range(bottomRight[1] - 1, topLeft[1], -1):
                solution.append(matrix[y_new][topLeft[0]])


            num_spirals += 1
        
        return solution
    
