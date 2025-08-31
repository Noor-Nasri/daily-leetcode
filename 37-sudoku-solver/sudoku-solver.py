class Solution:
    def solveStep(self, pos, valsInRow, valsInCols, valsInCubes):
        nextPos = (pos[0], pos[1] + 1)
        if pos == (9,0):
            return True
        elif pos[1] == 8:
            nextPos = (pos[0] + 1, 0)
        else:
            nextPos = (pos[0], pos[1] + 1)

        row, col = pos
        cube = (row // 3, col // 3)
        if self.board[row][col] != ".":
            return self.solveStep(nextPos, valsInRow, valsInCols, valsInCubes)

        for i in range(1, 10):
            if i not in valsInRow[row] and i not in valsInCols[col] and i not in valsInCubes[cube[0]][cube[1]]:
                valsInRow[row].add(i)
                valsInCols[col].add(i)
                valsInCubes[cube[0]][cube[1]].add(i)
                if self.solveStep(nextPos, valsInRow, valsInCols, valsInCubes):
                    self.board[row][col] = str(i)
                    return True
                
                valsInRow[row].remove(i)
                valsInCols[col].remove(i)
                valsInCubes[cube[0]][cube[1]].remove(i)
        
        return False



    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        valsInRow = [set() for r in range(9)]
        valsInCols = [set() for c in range(9)]
        valsInCubes = [[set() for c in range(3)] for r in range(3)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    cube = (row // 3, col // 3)
                    i = int(board[row][col])
                    valsInRow[row].add(i)
                    valsInCols[col].add(i)
                    valsInCubes[cube[0]][cube[1]].add(i)
        
        self.board = board
        self.solveStep((0, 0), valsInRow, valsInCols, valsInCubes)