class Solution:
    # Why wouldn't we just set as many 9s as possible, then leftover in a single val?
    # 9 is always better than 8 and 1, etc. 
    # I think thats all, pretty basic. 

    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9 < sum:
            return ""
        
        num9s = sum//9
        lastChar = sum - 9*num9s
        result = "9"*num9s
        if lastChar:
            result += str(lastChar)

        result += "0"*(num - len(result))

        return result
        