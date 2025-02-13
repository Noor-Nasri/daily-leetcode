from heapq import heapify, heappop, heappush

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        while nums[0] < k:
            num1 = heappop(nums)
            num2 = heappop(nums)
            heappush(nums, num1 * 2 + num2)
            operations += 1
        
        return operations
        