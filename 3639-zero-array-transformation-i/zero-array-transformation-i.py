class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        subs = [0 for i in range(len(nums))]
        cutoffs = [0 for i in range(len(nums))]
        for st, en in queries:
            subs[st] += 1
            cutoffs[en] += 1

        sub_total = 0
        for ind in range(len(nums)):
            sub_total += subs[ind]
            if nums[ind] - sub_total > 0:
                return False
            sub_total -= cutoffs[ind]

        return True
        