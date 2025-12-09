from math import comb
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        numCounts = {}
        pairCounts = {}
        totalFound = 0
        numZero = 0

        for num in nums:
            if num == 0:
                numZero += 1
                continue
            valDouble = int(num * 2)
            occurDouble = numCounts.get(valDouble, 0)
            pairCounts[(valDouble, num)] = pairCounts.get((valDouble, num), 0) + occurDouble

            if num % 2 == 0:
                newTriplets = pairCounts.get((num, num // 2), 0)
                totalFound += newTriplets
                totalFound %= 10**9 + 7
            
            numCounts[num] = numCounts.get(num, 0) + 1

        # inds of 0s dont matter, all 3 work
        if numZero >= 3:
            totalFound += comb(numZero, 3)
            totalFound %= 10**9 + 7


        return totalFound

            
        