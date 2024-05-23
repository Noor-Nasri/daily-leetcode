class Solution:
    def powHelper(self, x: float, n: int) -> float:
        if (n == 0): return 1
        if (n == 1): return x
        if (n in self.memoization): return self.memoization[n]

        cutOff = n // 2
        extra = n - cutOff
        ans = self.powHelper(x, cutOff) * self.powHelper(x, extra)
        self.memoization[n] = ans
        return ans

    def myPow(self, x: float, n: int) -> float:
        self.memoization = {}
        if n < 0:
            n *= -1
            x = 1/x
        return self.powHelper(x, n)
        