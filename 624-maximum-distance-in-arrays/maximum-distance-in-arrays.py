class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        candidates = []

        for arr_ind in range(len(arrays)):
            candidates.append((arrays[arr_ind][0], arr_ind))
            candidates.append((arrays[arr_ind][-1], arr_ind))
        
        candidates = sorted(candidates, key = lambda x : x[0])

        if candidates[0][1] != candidates[-1][1]:
            return candidates[-1][0] - candidates[0][0]
        
        return max(candidates[-1][0] - candidates[1][0], candidates[-2][0] - candidates[0][0])