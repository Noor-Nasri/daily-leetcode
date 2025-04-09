class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = {k}
        for num in nums:
            if num < k:
                return -1
            
            if not num in seen:
                seen.add(num)

        return len(seen) - 1
        