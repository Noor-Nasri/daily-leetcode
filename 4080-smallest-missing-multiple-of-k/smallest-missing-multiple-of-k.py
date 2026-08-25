class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        mult = 1

        while True:
            val = k*mult
            if val not in nums:
                return val
            
            mult += 1
