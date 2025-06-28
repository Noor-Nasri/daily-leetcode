class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Get k smallest values, then reput them back in order and return that
        items = [(nums[ind], ind) for ind in range(len(nums))]
        biggest_k = sorted(items, reverse = True)[:k]
        biggest_k = sorted([(e[1], e[0]) for e in biggest_k]) # flip it back to ind, val

        result = [e[1] for e in biggest_k]

        return result
