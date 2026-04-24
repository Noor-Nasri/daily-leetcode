class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dist = 0
        buffer = 0
        for move in moves:
            if move == "R":
                dist += 1
            elif move == "L":
                dist -= 1
            else:
                buffer += 1

        return abs(dist) + buffer 
        