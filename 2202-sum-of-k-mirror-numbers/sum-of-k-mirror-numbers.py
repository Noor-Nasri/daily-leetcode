# public sol, busy week
class Solution:

    def isKPalindrome(self, x: int, base: int) -> bool:
        digits = []
        while x > 0:
            digits.append(x % base)
            x //= base
        return digits == digits[::-1]

    def generatePalindromes(self, length: int) -> List[int]:
        result = []
        if length == 1:
            for i in range(1, 10):
                result.append(i)
            return result

        half = 10 ** ((length + 1) // 2)
        start = 10 ** ((length - 1) // 2)
        for i in range(start, half):
            s = str(i)
            if length % 2 == 0:
                p = s + s[::-1]
            else:
                p = s + s[-2::-1]
            result.append(int(p))
        return result

    def kMirror(self, k: int, n: int) -> int:
        result = []
        length = 1
        while len(result) < n:
            for p in self.generatePalindromes(length):
                if self.isKPalindrome(p, k):
                    result.append(p)
                    if len(result) == n:
                        return sum(result)
            length += 1
        return sum(result)