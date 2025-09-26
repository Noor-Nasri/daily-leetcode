class Solution:
    # triangles are any combo where a + b > c. Intuitively we can just do n^2 for a, b then do BS to get # of valid Cs.
    # Is there faster than n^2logn? Maybe not, since we will need to look at pairs to verify the equation anyways

    def firstIndGENum(self, nums, val):
        low = 0
        high = len(nums) - 1
        best = len(nums)

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= val:
                best = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return best

    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        combos = 0
        for a in range(len(nums)):
            if nums[a] == 0:
                continue

            for b in range(a + 1, len(nums)):
                total = nums[a] + nums[b]
                indFirstExclusion = self.firstIndGENum(nums, total)
                combos += indFirstExclusion - b - 1

        return combos