class Solution:
    # This seems like a fun O(n) sweep. We can just solve F(0) first
    # Then, shifting to F(1) means 1 less of every number, so minus sum(nums)
    # BUT, since Arr[0] went from 0 to -1 instead of (k - 1), we need to add Arr[i]*k
    # And just repeat the fullsweep!

    def maxRotateFunction(self, nums: List[int]) -> int:
        rawSum = sum(nums)
        rollingSum = 0
        for ind in range(len(nums)):
            rollingSum += ind * nums[ind]

        maximumValue = rollingSum
        for ind in range(1, len(nums)):
            rollingSum -= rawSum
            rollingSum += nums[ind - 1] * len(nums)
            maximumValue = max(maximumValue, rollingSum)
        
        return maximumValue