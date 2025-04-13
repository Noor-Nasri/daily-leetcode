# Idea: we can pick all palindromes by choosing the first half, thus only 10^5 max branches
# Then we store the count of digits as the hash to not overcount, and count all valid permutations of those digits
from math import factorial

class Solution:
    def numPermutations(self, digit_counts):
        # first digit can be anything but 0, then rest is (n-1)!
        # then need to remove double counting 
        allPerms = (self.n - digit_counts[0]) * factorial(self.n - 1)
        for val in digit_counts:
            allPerms //= factorial(val)

        return allPerms

    def countDigits(self, chosen_digits):
        counts = [0 for i in range(10)]
        for digStr in chosen_digits:
            counts[ord(digStr) - ord('0')] += 1
        return tuple(counts)

    def exploreAllPalindromes(self, num_chosen: int, chosen_digits):
        if num_chosen == self.n:
            val = int("".join(chosen_digits))
            digit_counts = self.countDigits(chosen_digits)
            
            if val % self.k == 0 and digit_counts not in self.seen:
                self.seen.add(digit_counts)
                self.totalFound += self.numPermutations(digit_counts)
        else:
            nextInd = num_chosen // 2
            numChanges = min(self.n - num_chosen, 2)
            for digit in range(10):
                if digit == 0 and num_chosen == 0:
                    continue # 0 cannot be the first decision, rest is okay

                newChoices = chosen_digits[:]
                newChoices[nextInd] = str(digit)
                newChoices[self.n - 1 - nextInd] = str(digit)
                self.exploreAllPalindromes(num_chosen + numChanges, newChoices)


    def countGoodIntegers(self, n: int, k: int) -> int:
        self.totalFound = 0
        self.seen = set()
        self.n = n
        self.k = k
        self.exploreAllPalindromes(0, [-1 for i in range(n)])
        return self.totalFound
