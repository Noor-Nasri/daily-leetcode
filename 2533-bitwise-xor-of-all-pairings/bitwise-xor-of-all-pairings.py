from math import log

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        tot = 0
        if len(nums2) % 2:
            for num in nums1:
                tot ^= num
        
        if len(nums1) % 2:
            for num in nums2:
                tot ^= num
                
        return tot