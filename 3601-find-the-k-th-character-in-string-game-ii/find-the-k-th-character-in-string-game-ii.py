class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # Since I did the easy version in log(n), it carries over to an easy solution here
        numIncrements = 0
        k -= 1
        while k > 0:
            prevOperationInd = int(log2(k))
            prevStrSize = 2 ** prevOperationInd
            numIncrements += operations[prevOperationInd]
            k -= prevStrSize

        resultChar = chr(97 + (numIncrements % 26))
        return resultChar
        