class Solution:
    def recurSearch(self, board, row, col, words, curWord, used, allFound):
        # Add word
        used.add((row, col))
        newWord = curWord + board[row][col]
        if newWord in words:
            allFound.add(newWord)
        
        if len(newWord) == 10: return
        
        # Expand in 4 directions
        if row > 0 and not (row - 1, col) in used:
            self.recurSearch(board, row - 1, col, words, newWord, set(used), allFound)
        
        if row < len(board) - 1 and not (row + 1, col) in used:
            self.recurSearch(board, row + 1, col, words, newWord, set(used), allFound)
        
        if col > 0 and not (row, col - 1) in used:
            self.recurSearch(board, row, col - 1, words, newWord, set(used), allFound)
        
        if col < len(board[0]) - 1 and not (row, col + 1) in used:
            self.recurSearch(board, row, col + 1, words, newWord, set(used), allFound)
        

        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        solutions = set()
        words = set(words)

        for row in range(len(board)):
            for col in range(len(board[0])):
                # Branch from this as the start
                used = set()
                self.recurSearch(board, row, col, words, "", used, solutions)
        

        return solutions
        