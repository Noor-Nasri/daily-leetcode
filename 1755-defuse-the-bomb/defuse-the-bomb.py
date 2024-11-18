class Solution:
    def getSum(self, code, ind, k, direction):
        tot = 0
        for i in range(1, k + 1):
            newInd = int((ind + i*direction) % len(code))
            tot += code[newInd]
        return tot

    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for i in range(len(code))]
        
        newList = []
        direction = k / abs(k)
        k = abs(k)

        for i, val in enumerate(code):
            newList.append(self.getSum(code, i, k, direction))
        return newList


        