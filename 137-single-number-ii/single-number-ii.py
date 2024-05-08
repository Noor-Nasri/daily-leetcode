class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # not sure how to do bit manipulation
        # will instead just use a set with minimal memory, then research

        seen = set()
        total_unique = 0
        total_all = 0
        for num in nums:
            total_all += num
            if num in seen: continue
            seen.add(num)
            total_unique += num
        
        return (total_unique*3 - total_all)//2
        