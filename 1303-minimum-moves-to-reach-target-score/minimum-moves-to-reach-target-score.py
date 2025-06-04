
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        numMoves = 0
        while target > 1 and maxDoubles:
            numMoves += 1 + (target % 2)
            target //= 2
            maxDoubles -= 1

        return numMoves + target - 1
        