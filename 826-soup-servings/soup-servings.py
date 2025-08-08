from math import ceil
class Solution:
    def dpSolve(self, remA, remB):
        if remA <= 0 and remB <= 0:
            return 0.5
        elif remA <= 0: # A finished first
            return 1
        elif remB <= 0:
            return 0
        
        if (remA, remB) in self.sols:
            return self.sols[(remA, remB)]
        
        options = [
            self.dpSolve(remA - 4, remB),
            self.dpSolve(remA - 3, remB - 1),
            self.dpSolve(remA - 2, remB - 2),
            self.dpSolve(remA - 1, remB - 3),
        ]

        self.sols[(remA, remB)] = sum(options)/4
        return self.sols[(remA, remB)]

    def soupServings(self, n: int) -> float:
        # Think of the problem as a race across n/25 buckets. 
        # Operation1: A moves up 4 steps
        # Operation2: A moves up 3 steps, B moves up 1
        # Operation3: A and B both move up 2 steps
        # Operation4: A moves up 1 step, B moves up 3
        # Can we just do DP? 10^9/25 buckets

        # Turns out, at n >= 4000, the answer is ~1 so we can just return it. Idk how tf we can realize that for a leetcode question
        if n >= 5000:
            return 1
        
        bucketsToDump = ceil(n / 25)
        self.sols = {}
        return self.dpSolve(bucketsToDump, bucketsToDump)



        