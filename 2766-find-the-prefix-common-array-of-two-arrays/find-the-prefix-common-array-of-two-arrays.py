class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        occurA = [False for i in range(51)]
        occurB = [False for i in range(51)]
        finalArray = []
        commonCount = 0

        for ind in range(len(A)):
            a, b = A[ind], B[ind]

            if not occurA[a] and occurB[a]:
                commonCount += 1
            occurA[a] = True

            if not occurB[b] and occurA[b]:
                commonCount += 1
            occurB[b] = True

            finalArray.append(commonCount)
        
        return finalArray
        