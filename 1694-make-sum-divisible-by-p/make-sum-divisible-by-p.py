class Solution:
    def getCutoffStartInd(self, inds, cutoffEndInd):
        # gets largest ind smaller than cutoff, or -1
        # my O(n) seems to be faster than O(logn) here lol
        for i in range(len(inds) - 1, -1 , -1):
            if inds[i] <= cutoffEndInd:
                return inds[i]

        return -1



    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p == 0: return 0
        # Setup prefix sums in O(n), then iterate backwards to pair them
        prefixSumIndices = {}
        tot = 0

        for ind in range(len(nums)):
            tot = (tot + nums[ind]) % p
            if tot in prefixSumIndices:
                prefixSumIndices[tot].append(ind)
            else:
                prefixSumIndices[tot] = [ind]
        
        # now go backwards
        best = -1
        tot = 0
        for ind_endOfCutoff in range(len(nums) - 1, - 1, -1):
            prev_sum_needed = (p - tot) % p
            #print("At ind", ind_endOfCutoff, "our total is", tot, "so we need", prev_sum_needed)

            if prev_sum_needed in prefixSumIndices or (ind_endOfCutoff != len(nums) - 1 and prev_sum_needed == 0):
                if prev_sum_needed in prefixSumIndices:
                    ind_startOfCutoff = self.getCutoffStartInd(prefixSumIndices[prev_sum_needed], ind_endOfCutoff)
                elif prev_sum_needed == 0:
                    ind_startOfCutoff = -1

                if ind_startOfCutoff > -1 or prev_sum_needed == 0:
                    possible_len = ind_endOfCutoff - ind_startOfCutoff
                    if best == -1 or possible_len < best:
                        best = possible_len
                        #print("improved best", best, "due to getting", prev_sum_needed, "from", ind_startOfCutoff, "and connecting with", ind_endOfCutoff)

            tot = (tot + nums[ind_endOfCutoff]) % p

        return best

        