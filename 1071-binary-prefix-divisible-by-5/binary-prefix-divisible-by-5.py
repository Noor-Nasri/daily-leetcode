class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curVal = 0
        for num in nums:
            curVal = curVal*2 + num
            ans.append(curVal % 5 == 0)
        
        return ans
        