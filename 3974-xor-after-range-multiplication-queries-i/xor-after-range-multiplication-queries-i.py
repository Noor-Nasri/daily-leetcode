class Solution:
    # Question is: per query: for range(l, r, k): array[ind] *= v
    # This would be at most O(n*q) which is 10^6. So we can just simulate.
    # We can optimize this for the xor but I'm sleepy, will just simulate

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for ind in range(l, r + 1, k):
                nums[ind] = (nums[ind] * v) % (10**9 + 7)
        
        tot = nums[0]
        for ind in range(1, len(nums)):
            tot ^= nums[ind]
        
        return tot