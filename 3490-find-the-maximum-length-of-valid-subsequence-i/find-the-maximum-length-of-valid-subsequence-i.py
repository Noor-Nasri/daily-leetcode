class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        #  wants all sums to be either all even or all odd
        # thus the subseq can either all be even, all be odd, or strictly alternating even and odd

        len_even = 0
        len_odd = 0
        len_alt = 0
        next_alt = nums[0]%2

        for num in nums:
            if num % 2 == 0:
                len_even += 1
            else:
                len_odd += 1
            
            if num % 2 == next_alt:
                next_alt = 1 - next_alt
                len_alt += 1

        return max(len_even, len_odd, len_alt)
        
        