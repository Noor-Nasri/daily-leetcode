class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        stateHistory = []
        curState = -1
        for ind in range(1, len(nums)):
            if nums[ind] == nums[ind - 1]:
                state = 0
            elif nums[ind] > nums[ind - 1]:
                state = 1
            else:
                state = 2
            if state != curState:
                curState = state
                stateHistory.append(curState)

        return stateHistory == [1, 2, 1]