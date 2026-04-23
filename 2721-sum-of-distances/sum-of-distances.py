class Solution:
    # First instinct is to group all inds of equal value. Now, how to compute the sum of diffs in O(n)?
    # Is it sufficient to just take (i - avg_ind) * num_vals? 
    # No .. because if they avg to your location, you're still supposed to get value from abs(i - real_ind)

    # So the real question is: Given i1, i2, i3, ... iN. How to get abs(i1 - i2) + abs(i1 - i3) + ...?
    # Maybe the trick is to compute the first one, then update in O(1) as we sweep.
    # Yes! Ie sum_0 -> sum_1 means we adjust by: shift_right*num_vals_left - shift_right*num_vals_right
    
    def groupInds(self, nums):
        valToInds = {}
        for ind in range(len(nums)):
            val = nums[ind]
            if val in valToInds:
                valToInds[val].append(ind)
            else:
                valToInds[val] = [ind]

        return list(valToInds.values())

    def distance(self, nums: List[int]) -> List[int]:
        finalArr = [-1 for i in range(len(nums))]
        groups = self.groupInds(nums)
        for groupedInds in groups:
            rollingSum = sum(groupedInds) - groupedInds[0]*len(groupedInds)
            finalArr[groupedInds[0]] = rollingSum

            for newInd in range(1, len(groupedInds)):
                shift = groupedInds[newInd] - groupedInds[newInd - 1]
                rollingSum += shift * (newInd*2 - len(groupedInds))
                finalArr[groupedInds[newInd]] = rollingSum

        return finalArr
