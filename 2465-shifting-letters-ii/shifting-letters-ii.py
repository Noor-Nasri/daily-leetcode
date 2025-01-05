class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        numShifts = [0 for i in range(len(s) + 1)]
        for st, en, d in shifts:
            shift = d*2-1
            numShifts[st] += shift
            numShifts[en + 1] -= shift

        actualShift = 0
        result = []
        for ind in range(len(s)):
            actualShift += numShifts[ind]
            letInd = (ord(s[ind]) - 97 + actualShift) % 26
            result.append(chr(letInd + 97))
        
        return "".join(result)
        