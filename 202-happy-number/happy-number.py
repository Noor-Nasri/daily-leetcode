class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(20):
            newNums = list(str(n))
            n = sum([int(e)**2 for e in newNums])
            if n == 1: 
                return True

        return False
        