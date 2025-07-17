class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        remainder_chains = [{} for i in range(len(nums))] #[ind] = {remainder = earliest next that makes it}

        for ind_first in range(len(nums)):
            for ind_second in range(ind_first + 1, len(nums)):
                rem = (nums[ind_first] + nums[ind_second]) % k
                if not rem in remainder_chains[ind_first]:
                    remainder_chains[ind_first][rem] = ind_second

        max_len = 0
        for rem in range(k):
            matches = {}
            for ind in range(len(nums)):
                if ind in matches: # prev chain welcomes us
                    len_arr = matches[ind] + 1
                else:
                    len_arr = 1
                
                if len_arr > max_len:
                    max_len = len_arr
                
                if rem in remainder_chains[ind]:
                    next_element = remainder_chains[ind][rem]
                    if (not next_element in matches) or (matches[next_element] < len_arr):
                        matches[next_element] = len_arr
        
                    

        return max_len

        