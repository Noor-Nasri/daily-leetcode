class Solution:
    def getCutoffStartInd(self, inds, cutoffEndInd):
        # gets largest ind smaller than cutoff, or -1
        low = 0
        high = len(inds) - 1
        best = -1

        while low <= high:
            mid = (low + high)//2
            if inds[mid] <= cutoffEndInd:
                best = inds[mid]
                low = mid + 1
            else:
                high = mid - 1

        return best



    def minSubarray(self, nums: List[int], p: int) -> int:
        # Setup prefix sums in O(n), then iterate backwards to pair them
        # When pairing the start and end indices, we do a O(logn) search. Thus nlogn
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

            if prev_sum_needed in prefixSumIndices or (ind_endOfCutoff != len(nums) - 1 and prev_sum_needed == 0):
                if prev_sum_needed in prefixSumIndices:
                    ind_startOfCutoff = self.getCutoffStartInd(prefixSumIndices[prev_sum_needed], ind_endOfCutoff)
                elif prev_sum_needed == 0:
                    ind_startOfCutoff = -1

                if ind_startOfCutoff > -1 or prev_sum_needed == 0:
                    possible_len = ind_endOfCutoff - ind_startOfCutoff
                    if best == -1 or possible_len < best:
                        best = possible_len
                        
            tot = (tot + nums[ind_endOfCutoff]) % p

        return best

        