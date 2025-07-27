class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # 2, 4, 1 --> Solves 4 as hill
        # sees another 1, then 6 --> Solves 1 as valley
        # So just keep going until the next new number, and decide for every 3 numbers

        lastNum = nums[0]
        ind = 1
        while ind < len(nums) and nums[ind] == lastNum: 
            ind += 1
        
        numFound = 0
        while ind < len(nums):
            midNum = nums[ind]
            while ind < len(nums) and nums[ind] == midNum: 
                ind += 1
            
            if ind < len(nums):
                if midNum > lastNum and midNum > nums[ind]:
                    numFound += 1
                elif midNum < lastNum and midNum < nums[ind]:
                    numFound += 1
                
            lastNum = midNum

        
        return numFound
        