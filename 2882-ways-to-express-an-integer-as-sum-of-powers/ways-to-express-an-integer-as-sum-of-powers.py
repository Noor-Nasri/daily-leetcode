class Solution:
    def solve(self, remVal, curNum):
        if (remVal, curNum) in self.sols:
            return self.sols[(remVal, curNum)]
        
        numWithPower = curNum ** self.x
        if numWithPower == remVal:
            return 1
        elif numWithPower > remVal:
            return 0

        ans = 0
        ans += self.solve(remVal, curNum + 1) % (10 ** 9 + 7)
        ans += self.solve(remVal - numWithPower, curNum + 1) % (10 ** 9 + 7)
        ans %= (10 ** 9 + 7)
        
        self.sols[(remVal, curNum)] = ans
        return ans

    def numberOfWays(self, n: int, x: int) -> int:
        # once x = 2, since n <= 300 the numbers we have to consider are <= 17. 
        # Cant we just do DP? (numToMatch, curNum). Always two options, include or not. 
        self.sols = {}
        self.x = x
        return self.solve(n, 1)