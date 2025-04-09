class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = {k}
        numOperations = 0
        for num in nums:
            if num < k:
                return -1
            
            seen.add(num)

        return len(seen) - 1
        