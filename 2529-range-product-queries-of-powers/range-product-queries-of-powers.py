from math import log2
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Just the binary, but can store it as vals to simplify here
        powers = []
        while n > 0:
            highestTwo = 2 ** int(log2(n))
            powers.append(highestTwo)
            n -= highestTwo
        
        powers = powers[::-1]
        prodArray = [1]
        for power in powers:
            prodArray.append(prodArray[-1] * power)
        
        answers = []
        for l, r in queries:
            ans = (prodArray[r + 1] // prodArray[l]) % (10 ** 9 + 7)
            answers.append(ans)
        
        return answers
