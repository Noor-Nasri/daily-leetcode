class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # After reading the bit-manipulation ideas, I submitted this
        """
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
        """

        # However, here is my actual solution which didn't have constant space
        seen = set()
        total_unique = 0
        total_all = 0
        for num in nums:
            total_all += num
            if num in seen: continue
            seen.add(num)
            total_unique += num
        
        return (total_unique*3 - total_all)//2