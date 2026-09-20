class Solution:
    # The answer can be n^2 so we clearly need to group things up.
    # My instinct is DP or some form of 2 pointer to grow and expand.
    # DP: (ind, diff) is also n^2... can we do some BS? No: ynnnyy has no len4 but has len5 
    # Okay I've gone in circles thinking about 2 pointer and segment tree ..

    # Wait can we literally just do D&C here? Solve(left) + Solve(right) + solve overlapping ones?
    # Yes, as long as we can solve for the number of subarrays that include the 2 middle ones in O(n)
    # What if the children solver tells us how many subarrays the edges are in, that are majority??
    # I think there is something here. Just need to iron it out

    # If we get a map from left/right that tells us: [t_diff] = [# num valid subarrays including the edge]
    # Then you can simply go through all diffs: Eg +5 from left can be paired with all subarrs >= -4 from right
    # Then to compute the diff for edges before return, you can just do a full sweep.
    # This should work in O(nlogn). Lets do it

    def solveBasicDiffMap(self, loopRange):
        diffMap = {}
        curDiff = 0
        for ind in loopRange:
            curDiff += self.singleDiff[ind]
            diffMap[curDiff] = diffMap.get(curDiff, 0) + 1
        return diffMap

    def solveTargetDiffs(self, left, right):
        # Returns: (numSubarrays with tdiff > 0, [tdiff] = # subarrays including left, [tdiff] = # subarrays including right)
        # Tdiff = 1 means there is one more target than non-targets, ie majority. 0 means tied, etc.

        if left == right:
            diffMap = {self.singleDiff[left]: 1}
            numValid = int(self.nums[left] == self.target)
            return [numValid, diffMap, diffMap]
        
        cutoff = (left + right) // 2
        validLeft, _, leftHalfMapWithLast = self.solveTargetDiffs(left, cutoff)
        validRight, rightHalfMapWithFirst, _ = self.solveTargetDiffs(cutoff + 1, right)

        # To compute overlap, we first need to precompute prefix sums for right, then iterate in order for left.
        nRightSubarraysGreaterThanDiff = {}
        potentialDiffRange = (right - left) // 2 + 1
        curCount = 0
        for diff in range(potentialDiffRange, -potentialDiffRange - 1, -1):
            nRightSubarraysGreaterThanDiff[diff] = curCount
            curCount += rightHalfMapWithFirst.get(diff, 0)
        
        #print("Looking at", left, "to", right, "the potential diff is", potentialDiffRange, "with right array", rightHalfMapWithFirst, "becoming", nRightSubarraysGreaterThanDiff)
        
        validMiddle = 0
        for diffFromLeft in leftHalfMapWithLast:
            # If we have 5, we just need right arrays > -5, so we end with >= 1
            # If we have -5, we need to get at least 6 more, etc.
            validMiddle += leftHalfMapWithLast[diffFromLeft] * nRightSubarraysGreaterThanDiff[-diffFromLeft]
        
        # Now we just need to solve our own mapWithFirst/mapWithLast by doing single sweeps
        diffMapWithFirst = self.solveBasicDiffMap(range(left, right + 1))
        diffMapWithLast = self.solveBasicDiffMap(range(right, left - 1, -1))
        validTotal = validLeft +  validRight + validMiddle

        return [validTotal, diffMapWithFirst, diffMapWithLast]

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        self.singleDiff = [e == target and 1 or -1 for e in nums]
        self.nums = nums
        self.target = target

        total, _, _ = self.solveTargetDiffs(0, len(nums) - 1)
        return total
        