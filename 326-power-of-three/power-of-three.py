class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        """
        for x in range(0, 1000000):
            ans = pow(3, x)
            if ans > n:
                return False
            elif ans == n:
                return True
        """
        low = 0
        high = 100
        while low <= high:
            mid = (low + high)//2
            ans = 3 ** mid
            if ans == n:
                return True
            elif ans < n:
                low =  mid + 1
            else:
                high = mid - 1
                   
        return False
