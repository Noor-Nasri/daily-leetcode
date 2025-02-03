class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestLen = 0
        
        lastNum = nums[0]
        curMode = 0
        curLen = 0

        for num in nums:
            if num == lastNum:
                curLen = 1
                curMode = 0
            
            elif num > lastNum:
                if curMode == 1:
                    curLen += 1
                else:
                    curMode = 1
                    curLen = 2
            
            else:
                if curMode == 2:
                    curLen += 1
                else:
                    curMode = 2
                    curLen = 2
            
            longestLen = max(longestLen, curLen)
            lastNum = num

        
        return longestLen

        