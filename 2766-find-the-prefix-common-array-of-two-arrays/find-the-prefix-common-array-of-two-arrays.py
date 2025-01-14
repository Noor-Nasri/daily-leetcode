class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA = set()
        seenB = set()
        total = 0

        result = []
        for ind in range(len(A)):
            a = A[ind]
            if a in seenB:
                total += 1
            else:
                seenA.add(a)
            
            b = B[ind]
            if b in seenA:
                total += 1
            else:
                seenB.add(b)
            
            result.append(total)
        
        return result