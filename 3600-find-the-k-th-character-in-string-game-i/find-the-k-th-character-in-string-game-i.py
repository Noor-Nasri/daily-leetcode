from math import log2

class Solution:
    def kthCharacter(self, k: int) -> str:
        # Sure we can brute force in n^2, but there is a log(n) solution here 
        # We keep doubling the size, so we just need to trace the ind back to figure out how many times it shifted
        # ex: ind = 5 <---> 6th element: 6 - 4 = 2. 2 - 2 = 0. So only two iterations
        numIncrements = 0
        k -= 1
        while k > 0:
            prevStrSize = 2 ** int(log2(k))
            k -= prevStrSize
            numIncrements += 1

        resultChar = chr(97 + (numIncrements % 26))
        return resultChar
