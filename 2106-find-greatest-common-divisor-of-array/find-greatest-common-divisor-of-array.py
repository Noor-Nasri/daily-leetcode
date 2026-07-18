class Solution:
    def simpleGcd(self, big, small):
        if small == 0:
            return big
        return self.simpleGcd(small, big % small)

    def findGCD(self, nums: List[int]) -> int:
        big = max(nums)
        small = min(nums)
        return self.simpleGcd(big, small)
        