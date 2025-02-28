class Solution:
    def lenOfSeqBasedOnStart(self, ind1, ind2):
        if (ind1, ind2) in self.sols:
            return self.sols[(ind1, ind2)]
        
        tot = self.arr[ind1] + self.arr[ind2]
        if tot not in self.indices:
            return 0
        
        ans = 1 + self.lenOfSeqBasedOnStart(ind2, self.indices[tot])
        self.sols[(ind1, ind2)] = ans
        return self.sols[(ind1, ind2)]


    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        indices = {}
        for ind in range(len(arr)):
            # arr is strictly increasing
            indices[arr[ind]] = ind 

        self.arr = arr
        self.indices = indices
        self.sols = {}
        
        longest = 0

        for ind1 in range(len(arr)):    
            for ind2 in range(ind1 + 1, len(arr)):
                longest = max(longest, self.lenOfSeqBasedOnStart(ind1, ind2))

        
        if longest == 0:
            return 0
        
        return longest + 2
