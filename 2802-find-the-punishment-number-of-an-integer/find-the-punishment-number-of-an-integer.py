class Solution:
    def __init__(self):
        # We already got AC with ~600ms on this solution
        # Since only 1k input, we can actually precompute this
        self.answers = []
        tot = 0
        for i in range(1, 1001):
            squared_digits =  [int(e) for e in str(i ** 2)]
            if self.canMatch(squared_digits, 0, i):
                tot += i**2
        
            self.answers.append(tot)
        

    def canMatch(self, digits, indStart, reqSum):
        if indStart == len(digits):
            return reqSum == 0

        if reqSum < 0:
            return False

        # all permutations is 2^j, but since j is just the number of digits, this is 2^7 = ~100
        curVal = 0
        for indEnd in range(indStart, len(digits)):
            curVal = curVal*10 + digits[indEnd]
            if self.canMatch(digits, indEnd + 1, reqSum - curVal):
                return True
        
        return False

    def punishmentNumber(self, n: int) -> int:
        return self.answers[n - 1]
