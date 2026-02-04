class Solution:
    # If this was only positive numbers, then we can simply track the states and sum history in O(n)
    # Since the sum can get negative, we may choose to abandon the current arr and start again. 
    # The problem is that in a sweep, the increasing numbers can be considered for arr1 or arr3.

    # We can still do this in a sweep but it's more complicated.
    # When the numbers are increasing, we maintain the maxSum for arr1.
    # At the same time, we check what happens when we end arr3.
    # When decreasing, we lock in the maxSum for arr1.

    def maxSumTrionic(self, nums: List[int]) -> int:
        curState = 0 # 1 is increasing, 2 is decreasing, 3 is increasing again
        maxSumForNextArr1 = 0
        maxSumForFinishedArr1 = 0
        sumForArr2 = 0
        curSumForArr3 = 0
        maxSum = -float('inf')

        for ind in range(1, len(nums)):
            if nums[ind] == nums[ind - 1]:
                curState = 0
            elif nums[ind] < nums[ind - 1]:
                if curState == 0:
                    pass 
                elif curState == 2:
                    sumForArr2 += nums[ind]
                else:
                    # Went from increasing to decreasing
                    maxSumForFinishedArr1 = maxSumForNextArr1
                    sumForArr2 = nums[ind]
                    curState = 2
            else:
                if curState == 0:
                    curState = 1
                    maxSumForNextArr1 = nums[ind - 1] + nums[ind]

                elif curState == 2:
                    # went from decreasing to increasing again
                    curState = 3
                    maxSumForNextArr1 = nums[ind - 1] + nums[ind]
                    curSumForArr3 = nums[ind]
                    option = maxSumForFinishedArr1 + sumForArr2 + curSumForArr3
                    maxSum = max(maxSum, option)

                else:
                    maxSumForNextArr1 = max(maxSumForNextArr1, nums[ind - 1]) + nums[ind]
                    if curState == 3:
                        curSumForArr3 += nums[ind]
                        option = maxSumForFinishedArr1 + sumForArr2 + curSumForArr3
                        maxSum = max(maxSum, option)
            
        return maxSum