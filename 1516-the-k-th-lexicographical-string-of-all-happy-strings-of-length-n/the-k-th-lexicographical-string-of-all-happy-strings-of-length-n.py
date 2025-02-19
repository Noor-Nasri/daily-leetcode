class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        numHappy = 3 * 2**(n - 1)
        if k > numHappy: return ""

        curStr = []
        lastChoice = 4
        while n:
            combosPerChar = 2**(n-1)
            charChoice = (k-1) // combosPerChar
            n -= 1
            k -= charChoice * combosPerChar

            if charChoice >= lastChoice:
                charChoice += 1 # cant pick same one twice, so leave a gap at the last choice
            
            curStr.append(chr(97 + charChoice))
            lastChoice = charChoice

        return "".join(curStr)
        