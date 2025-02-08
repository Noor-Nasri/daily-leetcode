class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToColor = {}
        numOfColor = {}
        allColors = set()
        results = []

        for x, col in queries:
            if x in ballToColor:
                col_old = ballToColor[x]
                numOfColor[col_old] -= 1

                if numOfColor[col_old] == 0:
                    allColors.remove(col_old)

            ballToColor[x] = col
            if col in numOfColor:
                numOfColor[col] += 1
            else:
                numOfColor[col] = 1
            allColors.add(col)
            
            results.append(len(allColors))

        return results
        