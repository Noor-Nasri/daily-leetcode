class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])

        lastArrow = points[0][1]
        numArrows = 1

        for i in range(1, len(points)):
            st, en = points[i]

            if st > lastArrow:
                # Not caught by last arrow, and earliest pop
                numArrows += 1
                lastArrow = en
        return numArrows
        