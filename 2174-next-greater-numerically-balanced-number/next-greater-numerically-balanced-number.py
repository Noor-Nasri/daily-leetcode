from itertools import permutations, combinations

class Solution:
    # Given the number of digits, we can find all possible balanced nums and check them
    # Smallest num for next digit count is just 1xx..xx
    # But what if they give a 6 digit number, and we can do a bigger 6 digit balanced num? 
    # Honestly this question is too annoying. I will brute force the permutations at the start and move on.
    # Actually, this isnt even brute force. This is an ideal solution lol.

    def __init__(self):
        baseDigits = [e*str(e) for e in range(1, 7)]
        allValidPerms = set()
        for nSelect in range(1, 7):
            charOptions = combinations(baseDigits, nSelect)
            for charCombination in charOptions:
                justChars = "".join(charCombination)
                if len(justChars) > 7:
                    continue
                
                for ordering in permutations(justChars):
                    allValidPerms.add("".join(ordering))
        
        self.balanced = sorted([int(e) for e in allValidPerms])

    def nextBeautifulNumber(self, n: int) -> int:
        l = 0
        h = len(self.balanced) - 1
        best = h
        while l <= h:
            m = (l + h)//2
            if self.balanced[m] > n:
                best = m
                h = m - 1
            else:
                l = m + 1


        return self.balanced[best]