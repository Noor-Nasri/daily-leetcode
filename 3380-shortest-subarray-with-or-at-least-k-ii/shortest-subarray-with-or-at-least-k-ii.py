class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # A bit is active if at least one element has it. So enable/disable bits
        # Basic sliding window to find shortest by finding possible then shortening it
        if k == 0: return 1

        best = -1
        ind_start = 0
        ind_end = 0
        cur_bit_counts = [0 for i in range(32)]
        def bitValue():
            return int("".join(str(min(e, 1)) for e in cur_bit_counts), 2)

        def adjustValue(num, multiplier):
            vals = [int(e) for e in str(bin(num))[2:]]
            offset = 32 - len(vals)
            for ind in range(len(vals)):
                cur_bit_counts[offset + ind] += vals[ind] * multiplier

        while (ind_end < len(nums)):
            adjustValue(nums[ind_end], 1)
            ind_end += 1

            while bitValue() >= k:
                length = ind_end - ind_start
                if best == -1 or best > length:
                    best = length
                    if best == 1: return 1
                

                adjustValue(nums[ind_start], -1)
                ind_start += 1

        
        return best




        