class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distA, distB = abs(x - z), abs(y - z)
        if distA == distB:
            return 0
        elif distA < distB:
            return 1
        else:
            return 2