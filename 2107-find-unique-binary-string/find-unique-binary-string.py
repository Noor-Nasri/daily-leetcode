class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        taken = set(nums)
        for i in range(n + 1):
            binStr = bin(i)[2:]
            binStr = "0"*(n - len(binStr)) + binStr
            if binStr not in taken:
                return binStr
        
        assert(False)

