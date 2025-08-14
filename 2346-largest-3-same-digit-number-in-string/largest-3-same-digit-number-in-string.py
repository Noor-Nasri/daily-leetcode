class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            substr = str(i)*3
            if substr in num:
                return substr
        
        return ""
        