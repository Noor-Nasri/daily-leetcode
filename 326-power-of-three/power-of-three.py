class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        for x in range(0, 1000000):
            ans = pow(3, x)
            if ans > n:
                return False
            elif ans == n:
                return True
                   
