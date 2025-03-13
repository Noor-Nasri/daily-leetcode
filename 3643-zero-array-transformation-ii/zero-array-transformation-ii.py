class Solution: 
    # Idea 1: Binary search and have a "canBeSolvedWithUpToK"
    # canBeSolvedWithUpToK seems difficult: 
        # Greedy approach, take earliest end at each ind: doesnt work because we may need longe
        # DP approach: Still need to consider all queries, so time complexity nk = nq
        # Heap idea: take the query with the most range first. But maybe we need the shorter ones ..
    
    # Idea 2: Realization - The moment 0 array is achieved, all other queries break it.
    # So use binary search, but just check exactly k. If "incomplete", can disregard everything before.
    # If "complete", it is solved, you don't need later ones. Easy!

    def canBeSolvedAtK(self, nums, queries, k):
        adjustments = [0 for i in range(len(nums) + 1)]
        for ind_q in range(k):
            s, e, v = queries[ind_q]
            adjustments[s] -= v
            adjustments[e + 1] += v

        curBonus = 0
        for ind_n in range(len(nums)):
            curBonus += adjustments[ind_n]
            newVal = nums[ind_n] + curBonus
            if newVal > 0:
                return False
        
        return True


    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        low = 0
        high = len(queries)
        best = -1

        while low <= high:
            mid = (low + high) // 2

            if self.canBeSolvedAtK(nums, queries, mid):
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return best