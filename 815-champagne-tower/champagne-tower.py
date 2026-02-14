class Solution:
    # We should measure how much has poured into any given cup
    # So amount(cup) = overflow(amount(leftParent))/2 + overflow(amount(rightParent))/2
    # This recursively goes up until the only parent is the root, which overflows at poured - 1
    # So this is jut DP: (depth_level, col) -> value. O(n^2) with n <= 100

    def overflowValue(self, depth_level, col_ind):
        uid = (depth_level, col_ind)
        if uid in self.sols:
            return self.sols[uid]
        elif depth_level == 0 and col_ind == 0:
            return max(0, self.poured - 1)
        elif col_ind < 0 or col_ind > depth_level:
            return 0
        
        recieved = (self.overflowValue(depth_level - 1, col_ind - 1) + self.overflowValue(depth_level - 1, col_ind))/2
        self.sols[uid] = max(0, recieved - 1)
        return self.sols[uid]

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0 and query_glass == 0:
            return min(1, poured)

        self.sols = {}
        self.poured = poured
        self.overflowValue(query_row, query_glass)
        recieved = (self.overflowValue(query_row - 1, query_glass - 1) + self.overflowValue(query_row - 1, query_glass))/2

        return min(1, recieved)