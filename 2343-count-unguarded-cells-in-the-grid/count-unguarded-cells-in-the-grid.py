class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        activeMatrix = [[1 for col in range(n)] for row in range(m)]
        all_guards = set([tuple(e) for e in guards])
        all_walls = set([tuple(e) for e in walls])

        # First pass: solve down and right
        rows_in_sight = set()
        cols_in_sight = set()
        for row in range(m):
            for col in range(n):
                #print("Looking at", row, col)
                if (row, col) in all_guards:
                    #print("Guard!")
                    activeMatrix[row][col] = 0
                    rows_in_sight.add(row)
                    cols_in_sight.add(col)
                elif (row, col) in all_walls:
                    #print("Wall!")
                    activeMatrix[row][col] = 0
                    rows_in_sight.discard(row)
                    cols_in_sight.discard(col)
                elif row in rows_in_sight or col in cols_in_sight:
                    #print("Seen!")
                    activeMatrix[row][col] = 0
        
        #print(activeMatrix)

        # Now solve upwards
        rows_in_sight = set()
        cols_in_sight = set()
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if (row, col) in all_guards:
                    activeMatrix[row][col] = 0
                    rows_in_sight.add(row)
                    cols_in_sight.add(col)
                elif (row, col) in all_walls:
                    activeMatrix[row][col] = 0
                    rows_in_sight.discard(row)
                    cols_in_sight.discard(col)
                elif row in rows_in_sight or col in cols_in_sight:
                    activeMatrix[row][col] = 0

        #print(activeMatrix)
        return sum([sum(e) for e in activeMatrix])

                

        