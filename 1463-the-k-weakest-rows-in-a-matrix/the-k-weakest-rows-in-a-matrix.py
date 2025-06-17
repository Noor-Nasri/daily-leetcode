from heapq import heapify, heappop
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for ind_row in range(len(mat)):
            n_soldiers = mat[ind_row].count(1)
            rows.append((n_soldiers * 100 + ind_row, ind_row))
            # priority: n_soldiers * 100 + row
        
        heapify(rows)
        ans = []
        for i in range(k):
            _, ind_row = heappop(rows)
            ans.append(ind_row)
        
        return ans