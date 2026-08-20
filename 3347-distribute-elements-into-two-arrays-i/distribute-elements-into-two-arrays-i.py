class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for ind in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[ind])
            else:
                arr2.append(nums[ind])
        
        return arr1 + arr2