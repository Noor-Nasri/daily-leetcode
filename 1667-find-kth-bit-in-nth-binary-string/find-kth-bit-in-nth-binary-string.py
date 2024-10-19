class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        digits = [0]
        for it in range(n - 1):
            digits.append(1)
            # add the inverse in reverse
            for ind in range(len(digits) - 2, -1, -1):
                digits.append(1 - digits[ind])
        
        return str(digits[k-1])
        