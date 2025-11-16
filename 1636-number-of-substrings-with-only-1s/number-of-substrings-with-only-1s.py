class Solution:
    def countSubArrsWithoutZeros(self, s):
        totalSubarr = 0
        oneCount = 0
        for c in s:
            if c == '1':
                oneCount += 1
            else:
                totalSubarr += oneCount * (oneCount + 1)/2
                oneCount = 0
        
        totalSubarr += oneCount * (oneCount + 1)/2
        #print(totalSubarr, "found without 0s")
        return totalSubarr

    def numSub(self, s: str) -> int:
        return int(self.countSubArrsWithoutZeros(s)) % (10**9 + 7)
        