class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        lastSeen = {}
        for i in range(len(nums)):
            lastSeen[nums[i]] = i

        solutions = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                needed = -(nums[i] + nums[j])
                if needed in lastSeen and lastSeen[needed] > j:
                    solutions.add((nums[i], nums[j], needed))
        
        return solutions
        