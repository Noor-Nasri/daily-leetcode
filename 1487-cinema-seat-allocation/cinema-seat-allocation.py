class Solution:
    # So this seems simple. Each row we try to put 2->5 and 6->9. Both no: try 4->7.
    # Can check this by just iterating in each row. O(grid). No issues.

    # AH, the catch! n is 10^9, so we cant iterate on the grid. 
    # The trick is still simple though: At most 10^4 reserved seats
    # So we only check the rows with reserved seats. All others = 2 * count

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        taken = {} # Prefix sum dict with only the relevant rows
        for row, col in reservedSeats:
            if row not in taken:
                taken[row] = [0 for i in range(10)]
            taken[row][col - 1] += 1

        for row in taken:
            for ind in range(1, 10):
                taken[row][ind] += taken[row][ind - 1]

        totalGroups = 2*(n - len(taken))
        for row in taken:
            leftAvail = not (taken[row][4] - taken[row][0])
            middleAvail = not (taken[row][6] - taken[row][2])
            rightAvail = not (taken[row][8] - taken[row][4])
            if leftAvail and rightAvail:
                totalGroups += 2
            elif leftAvail or middleAvail or rightAvail:
                totalGroups += 1
            
        return totalGroups