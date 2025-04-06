class Solution:
    def maxNumElements(self, curInd):
        if curInd in self.sols:
            return self.sols[curInd]

        maxNum = 1
        for ind in range(curInd + 1, len(self.nums)):
            if self.nums[ind] % self.nums[curInd] == 0:
                option = 1 + self.maxNumElements(ind)
                maxNum = max(maxNum, option)

        self.sols[curInd] = maxNum
        return maxNum


    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # need new number to be a multiple of all existing numbers. We can store this as the latest number 
        self.nums = sorted(nums)
        self.sols = {}

        maxFound = [-1, None]
        for ind in range(len(nums)):
            result = self.maxNumElements(ind)
            if result > maxFound[0]:
                maxFound = [result, ind]
        
        # now backtrack to get set of numbers
        included = set()
        numNodes, curInd = maxFound
        while numNodes:
            included.add(self.nums[curInd])
            numNodes -= 1
            for ind2 in range(curInd + 1, len(self.nums)):
                if self.nums[ind2] % self.nums[curInd] == 0 and self.sols[ind2] == numNodes:
                    curInd = ind2
                    break
        
        # return answer in same relative order
        finalArr = []
        for num in nums:
            if num in included:
                finalArr.append(num)
        
        return finalArr