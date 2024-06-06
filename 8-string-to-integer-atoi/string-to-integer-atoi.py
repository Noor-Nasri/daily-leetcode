class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        num = []
        sign = None

        for char in s:
            if '0' <= char <= '9':
                num.append(char)
            elif (char == '-' or char == '+') and sign == None:
                sign = (char == '+')*2-1 # 1 and -1
            else:
                break

            if sign == None:
                sign = 1
        
        if not num: return 0
        if sign==None: sign = 1

        val = int("".join(num)) * sign

        if val < -pow(2, 31): return -pow(2, 31)
        if val >= pow(2, 31): return pow(2, 31) - 1
        return val
    
        