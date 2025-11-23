class Solution:
    # Seems like a classic DP: at each ind we can include the num or not
    # The trick is to group by remainder instead of current sum. So if we take 5, now we need total sum with remainder 1. 

    def maxSumFromIndWithRemX(self, ind, x):
        # returns -1 if desired remainder is impossible
        if (ind, x) in self.sols:
            return self.sols[(ind, x)]
        elif ind == len(self.nums):
            if x == 0:
                return 0
            else:
                return -1
        
        indRem = self.nums[ind] % 3
        remNeeded = (x - indRem) % 3
        op1 = self.maxSumFromIndWithRemX(ind + 1, remNeeded)
        if op1 >= 0:
            op1 += self.nums[ind]

        op2 = self.maxSumFromIndWithRemX(ind + 1, x)
        self.sols[(ind, x)] = max(op1, op2)
        return self.sols[(ind, x)]

    def maxSumDivThree(self, nums: List[int]) -> int:
        self.sols = {}
        self.nums = nums
        return self.maxSumFromIndWithRemX(0, 0)