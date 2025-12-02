class Solution:
    # So for any 2 points with the same y, we can then create a horizontal trapezoid by picking any 2 points of another y.
    # Given # of points for a specific y, we get nC2 combos that can be paired with other lines
    # nC2 = n * (n-1) / 2
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MODVAL = 10**9 + 7
        countsPerLine = {}
        for x, y in points:
            countsPerLine[y] = countsPerLine.get(y, 0) + 1

        found = 0
        curViableCombos = 0
        for y in sorted(list(countsPerLine.keys())):
            if countsPerLine[y] < 2:
                continue

            numLinesOnY = countsPerLine[y] * (countsPerLine[y] - 1) // 2
            found = (found + ((numLinesOnY * curViableCombos) % MODVAL)) % MODVAL
            curViableCombos = (curViableCombos + numLinesOnY) % MODVAL
        
        return int(found)