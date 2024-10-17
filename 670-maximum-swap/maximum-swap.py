class Solution:
    def maximumSwap(self, num: int) -> int:
        # we just want to find the highest digit, and pull it from the right most occurance
        # then swap that digit with out first digit to make biggest change
        str_num = str(num)
        digits = [int(e) for e in str_num][::-1]
        
        while digits and max(digits) == digits[-1]:
            digits.pop()
        
        if len(digits) >= 2:
            # swap first occurance of max with [-1], because -1 is actually the start of number
            ind_best = digits.index(max(digits))
            val = digits[ind_best]
            digits[ind_best] = digits[-1]
            digits[-1] = val
        
        final_str = str_num[:len(str_num) - len(digits)] + "".join([str(e) for e in digits[::-1]])
        return int(final_str)
