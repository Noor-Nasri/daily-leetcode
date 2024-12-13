class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = []
        for ch in s:
            newNum = ord(ch) - ord('a') + 1
            for dig in str(newNum):
                digits.append(int(dig))
        
        for i in range(k - 1):
            newNum = sum(digits)
            digits = [int(e) for e in str(newNum)]

        return sum(digits)