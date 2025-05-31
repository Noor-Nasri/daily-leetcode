from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # First flatten the board
        portals = [-1]
        for row in range(len(board) -1, -1, -1):
            for col in range(len(board)):
                if (len(board) - row) % 2 == 0:
                    col = len(board) - 1 - col
                portals.append(board[row][col])
        
        # Now basic bfs
        target = len(board) ** 2
        seen = {1}
        cur = deque([1])
        depth = 0
        while cur:
            for _ in range(len(cur)):
                node = cur.popleft()
                for nextNode in range(node + 1, min(target + 1, node + 7)):
                    if portals[nextNode] != -1:
                        nextNode = portals[nextNode]

                    if nextNode == target:
                        return depth + 1
                    elif nextNode not in seen:
                        seen.add(nextNode)
                        cur.append(nextNode)

            depth += 1

        return -1
        