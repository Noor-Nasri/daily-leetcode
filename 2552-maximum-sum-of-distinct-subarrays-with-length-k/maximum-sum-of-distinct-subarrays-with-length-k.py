class Solution:
    def addNum(self, num):
        if num in self.seen:
            self.seen[num] += 1
            self.duplicatedKeys.add(num)
        else:
            self.seen[num] = 1
        self.total += num

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxTotal = 0
        self.total = 0
        self.seen = {}
        self.duplicatedKeys = set()


        for i in range(k - 1):
            self.addNum(nums[i])

        for ind in range(k - 1, len(nums)):
            self.addNum(nums[ind])
            if not self.duplicatedKeys:
                maxTotal = max(maxTotal, self.total)
            
            numToExclude = nums[ind - k + 1]
            self.seen[numToExclude] -= 1
            self.total -= numToExclude
            if self.seen[numToExclude] == 1:
                self.duplicatedKeys.remove(numToExclude)
            elif self.seen[numToExclude] == 0:
                del self.seen[numToExclude]
        
        return maxTotal

