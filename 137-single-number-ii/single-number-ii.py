class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Originally did this question with a minimal set (beats 80%)
        # After reading the bit-manipulation ideas, I adjusted this
        # We want to count number of 1s across each bit
        # When the real bit is 1, the total has remainder 1 (from %3)

        total = 0
        for i in range(32):
            num_1s = 0
            for num in nums:
                # num >> i shifts the binary i times to the RIGHT
                # that means, the wanted one will be at the last position
                # ie least significant. So then we AND with 1 to just get the last
                is_1 = (num >> i) & 1
                num_1s += is_1

            # Can also just total += 2**(..)
            power_2 = (num_1s % 3) << i
            total |= power_2

        if total >= 2**31: total -= 2**32
        return total
        