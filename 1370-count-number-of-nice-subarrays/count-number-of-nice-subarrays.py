class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        inds_odd = []
        for ind in range(len(nums)):
            if nums[ind] % 2 == 1:
                inds_odd.append(ind)
        
        # [0], [1], [3], 4
        # len(inds_odd) = 4 k = 3 --> 0, 1
        num_valid = 0
        for i in range(len(inds_odd) - k + 1):
            ind_of_prev_odd = (i == 0) and -1 or inds_odd[i - 1]
            ind_of_next_odd = (i + k == len(inds_odd)) and len(nums) or inds_odd[i + k]
            
            valid_start = inds_odd[i] - ind_of_prev_odd
            valid_end = ind_of_next_odd - inds_odd[i + k - 1]
            num_valid += valid_start * valid_end

        return num_valid