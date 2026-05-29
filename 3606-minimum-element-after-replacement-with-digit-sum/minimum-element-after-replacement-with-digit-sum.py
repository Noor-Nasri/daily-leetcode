class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min([sum([int(e) for e in str(val)]) for val in nums])