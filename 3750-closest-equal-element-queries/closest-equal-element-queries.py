class Solution:
    # We can group up indices with the same value, then assign shortest dists within each bucket
    # This is two simple O(n) sweeps: Sort into buckets, then each value is min(distL, distR)
    # Then we know the answer for all inds, and can just use it for the query

    def circleDist(self, ind1, ind2):
        return min(abs(ind2 - ind1), min(ind1, self.n - ind1) + mind)
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        valueToInds = {}
        for ind in range(len(nums)):
            val = nums[ind]
            if val in valueToInds:
                valueToInds[val].append(ind)
            else:
                valueToInds[val] = [ind]
        
        finalDists = [-1 for i in range(len(nums))]
        for value in valueToInds:
            indList = valueToInds[value]
            if len(indList) == 1:
                continue
            
            for indWithinIndList in range(len(indList)):
                indPrev = indList[(indWithinIndList - 1) % len(indList)]
                ind = indList[indWithinIndList]
                if indPrev < ind:
                    distLeft = ind - indPrev
                else:
                    distLeft = ind + (len(nums) - indPrev)

                indNext = indList[(indWithinIndList + 1) % len(indList)]
                if indNext > ind:
                    distRight = indNext - ind
                else:
                    distRight = indNext + (len(nums) - ind)
                    
                finalDists[ind] = min(distLeft, distRight)

        return [finalDists[e] for e in queries]