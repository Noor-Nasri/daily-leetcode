class Solution:
    # There are only 720 possible board states. We need to make a graph between them, then its just a basic BFS.
    # Can even prestore all 720 answers. 
    def makeBoards(self, board, rem_choices):
        if not rem_choices:
            return [board]
        
        boards = []
        for choice in rem_choices:
            new_board = board[::]
            new_board.append(choice)
            new_choices = rem_choices[::]
            new_choices.remove(choice)
            boards.extend(self.makeBoards(new_board, new_choices))

        return boards
    
    def makeConnections(self, boards):
        newBoards = {}
        for board in boards:
            vals = tuple(board)
            conns = []
            
            cur_loc = board.index(0)

            if cur_loc != 0 and cur_loc != 3:
                new_board = board[:]
                new_board[cur_loc] = new_board[cur_loc - 1]
                new_board[cur_loc - 1] = 0
                conns.append(tuple(new_board))
            
            if cur_loc != 2 and cur_loc != 5:
                new_board = board[:]
                new_board[cur_loc] = new_board[cur_loc + 1]
                new_board[cur_loc + 1] = 0
                conns.append(tuple(new_board))

            if cur_loc < 3:
                new_board = board[:]
                new_board[cur_loc] = new_board[cur_loc + 3]
                new_board[cur_loc + 3] = 0
                conns.append(tuple(new_board))

            if cur_loc >= 3:
                new_board = board[:]
                new_board[cur_loc] = new_board[cur_loc - 3]
                new_board[cur_loc - 3] = 0
                conns.append(tuple(new_board))

            newBoards[vals] = conns
        
        return newBoards

    
    def __init__(self):
        self.boards = self.makeBoards([], [i for i in range(6)])
        self.conns = self.makeConnections(self.boards)

    def solve(self, cur_board):
        golden = tuple([1, 2, 3, 4, 5, 0])
        seen = {cur_board}
        cur_iter = [cur_board]
        num_iter = 0
        while cur_iter:
            next_iter = []
            for board in cur_iter:
                if board == golden: return num_iter
                for conn in self.conns[board]:
                    if conn in seen: continue
                    seen.add(conn)
                    next_iter.append(conn)

            num_iter += 1
            cur_iter = next_iter
        
        return -1

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        return self.solve(tuple(board[0] + board[1]))
        