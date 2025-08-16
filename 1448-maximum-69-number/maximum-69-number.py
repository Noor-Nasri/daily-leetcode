class Solution:
    def maximum69Number (self, num: int) -> int:
        numStr = str(num)
        for ind in range(len(numStr)):
            if numStr[ind] == '6':
                return int(numStr[:ind] + "9" + numStr[ind + 1:])

        return num
        