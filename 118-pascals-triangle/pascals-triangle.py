class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for r in range(numRows - 1):
            nextRow = [1]
            for ind in range(len(rows[-1]) - 1):
                nextRow.append(rows[-1][ind] + rows[-1][ind + 1])
            nextRow.append(1)
            rows.append(nextRow)

        return rows