class Solution:
    def hasSameDigits(self, s: str) -> bool:
        cur = [int(e) for e in s]
        while len(cur) > 2:
            nextLevel = []
            for ind in range(len(cur) - 1):
                newNum = (cur[ind] + cur[ind + 1]) % 10
                nextLevel.append(newNum)

            cur = nextLevel
            
        return len(cur) == 2 and cur[0] == cur[1]
        