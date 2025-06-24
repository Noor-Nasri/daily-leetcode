class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        seen = [0 for i in range(len(nums) + 1)]
        for ind, val in enumerate(nums):
            if val == key:
                seen[max(0, ind - k)] += 1
                seen[min(ind + k + 1, len(nums))] -= 1
        
        results = []
        curSum = 0
        for ind, val in enumerate(seen):
            curSum += val
            if curSum:
                results.append(ind)
        
        return results