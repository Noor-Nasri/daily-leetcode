class Solution:
    def search(self, board, word, row, col, ind) ->bool:
        # ind is for the char we are going to look for in neighbours
        if ind == len(word): return True
        possible = []
        if row > 0: possible.append((row - 1, col))
        if row < len(board) - 1: possible.append((row + 1, col))
        if col > 0: possible.append((row, col - 1))
        if col < len(board[0]) - 1: possible.append((row, col + 1))

        for neighbor in possible:
            row2, col2 = neighbor
            if board[row2][col2] == word[ind]:
                cur = board[row][col]
                board[row][col] = '/' # remove it for now
                check = self.search(board, word, row2, col2, ind+1)
                board[row][col] = cur
                if check: return True

        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[row])):
                char = board[row][col]
                if char == word[0]: # Try branching from here
                    if self.search(board, word, row, col, 1): return True
        
        return False

        