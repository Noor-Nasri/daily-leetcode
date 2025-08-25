class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # (0, 0) then (0, 1), (0, 1), then (2, 0), (1, 1), (0, 2), then (1, 2), (2, 1), then (2, 2)
        # By going diag, we the positions all have the same sum. So we just go up one sum at a time, and flip the start each time

        arr = []
        for pos_sum in range(len(mat) + len(mat[0]) - 1):
            # pos_sum = 4 but only 3x3, meaning only (2,2) is valid
            # So we want to only visit row 2 there
            min_row = max(0, pos_sum - len(mat[0]) + 1)
            max_row = min(len(mat) - 1, pos_sum)

            if pos_sum % 2:
                ordered_range = range(min_row, max_row + 1)
            else:
                ordered_range = range(max_row, min_row - 1, -1)

            for row in ordered_range:
                col = pos_sum - row
                arr.append(mat[row][col])

        return arr
        