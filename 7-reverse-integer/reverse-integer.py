class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        digits = list(str(x))[::-1]
        if is_neg: digits.pop()

        # 2^31 stored as digits
        MAX_VALUE = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
        if len(digits) > len(MAX_VALUE): return 0
        if len(digits) < len(MAX_VALUE):
            rev_int = int("".join(digits))
            if is_neg: rev_int*= -1
            return rev_int
        
        for ind in range(len(MAX_VALUE)):
            cur_digit = int(digits[ind])
            max_digit = MAX_VALUE[ind]

            if cur_digit > max_digit:
                return 0
            
            if cur_digit < max_digit:
                rev_int = int("".join(digits))
                if is_neg: rev_int*= -1
                return rev_int

        # Fully equal to max
        if is_neg:
            return -2147483648
        return 0
                
        
        