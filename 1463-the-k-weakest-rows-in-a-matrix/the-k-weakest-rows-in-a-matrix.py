class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for ind_row in range(len(mat)):
            n_soldiers = mat[ind_row].count(1)
            rows.append((n_soldiers, ind_row))
        
        rows = sorted(rows, key = lambda x: x[0] * 100 + x[1])
        ans = []
        for _, ind_row in rows:
            ans.append(ind_row)
            if len(ans) == k:
                break
        
        return ans