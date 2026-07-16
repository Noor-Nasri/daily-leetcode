class Solution:
    # Okay so I just need to keep taking gcds, whats the trick here ..
    # gcd(a, b) can be solved in log(min(a, b)) with the euclidean algo
    # So do I just do that n + n/2 times? I guess it'll work

    def simpleGcd(self, large, small):
        # Imagine (48, 18). 48 = 18 + 18 + 12 so remainder 12
        # The GCD must already divide into 18, so for it to also divide 48 it must also divide 12
        if small == 0:
            return large
        
        return self.simpleGcd(small, large % small)

    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        curMax = 0

        for num in nums:
            curMax = max(curMax, num)
            prefixGcd.append(self.simpleGcd(curMax, num))
        
        prefixGcd = sorted(prefixGcd)
        total = 0
        for ind in range(len(prefixGcd) // 2):
            total += self.simpleGcd(prefixGcd[-ind-1], prefixGcd[ind])
        
        return total
