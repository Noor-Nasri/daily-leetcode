class Solution:
    def bsForSE(self, nums, start_ind, value):
        # Get the last index where nums[i] <= value. We know there is a solution
        low = start_ind
        high = len(nums) - 1

        while low <= high:
            mid = ceil((low + high)/2)
            if nums[mid] <= value:
                if mid == high: 
                    return mid
                low = mid
            else:
                high = mid - 1

    def bsForGE(self, nums, start_ind, value):
        # Get the first index where nums[i] >= value. We know there is a solution
        low = start_ind
        high = len(nums) - 1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= value:
                if mid == low: 
                    return mid
                high = mid
            else:
                low = mid + 1


    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        solutions = 0
        nums = sorted(nums)
        #print(nums)
        for ind in range(len(nums) - 1):
            val_small = nums[ind]
            if val_small + nums[ind + 1] > upper or val_small + nums[-1] < lower:
                continue # 0 solutions possible
            
            range_start = self.bsForGE(nums, ind + 1, lower - val_small)
            range_end = self.bsForSE(nums, ind + 1, upper - val_small)
            #print("For val", val_small, "we have this range of pairs:", range_end, range_start)
            solutions += range_end - range_start + 1
        
        return solutions
            