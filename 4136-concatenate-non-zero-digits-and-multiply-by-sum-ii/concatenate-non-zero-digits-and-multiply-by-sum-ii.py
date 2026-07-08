class Solution:
    # So for every [l, r] we need to immediately know the new concat and the new digit sum
    # Digit sum for s[l..r] is easy, just use prefix sums

    # For concat, can we also do a prefix sum variation? 
    # What if we create the full concat, and each [ind] points to its location?
    # The first problem is we cant even store the full concat as an int.
    # If we store as string, then even if we know the two inds we need to then re-slice

    # Suppose s=10203004. 3->5 should be 23. What we can do is:
    # [5] has 123 --> 3 sigdigs
    # [2] has 1 --> 1 sigsig
    # In this case, we would just subtract 1*100 (elevate [2] to same num of digits)
    # The trouble is only with mod: If each ind stores s[0..i] % MOD, how to reconsile?
    # We want to solve for: (s[0..r] - s[0..l]*multiplier) % MOD
    # = (s[0..r] % MOD - s[0..l]*multiplier % MOD) % MOD
    # = ( s[0..r] % MOD - (s[0..l] % MOD)*(multiplier % MOD) % MOD) % MOD
    # = (prefixR - prefixL * (prefixDiff % MOD) % MOD) % MOD

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        curDigSum, curDigCount, curConcat = 0, 0, 0
        digitSums = [0] # All inds shifted by 1 so that [0] is before anything is included
        digitCounts = [0]
        concats = [0]

        for numChar in s:
            digit = int(numChar)
            if digit:
                curDigSum += digit
                curDigCount += 1
                curConcat = (curConcat * 10 + digit) % MOD

            digitSums.append(curDigSum)
            digitCounts.append(curDigCount)
            concats.append(curConcat)

        answers = []
        for l, r in queries:
            numDigits = digitCounts[r + 1] - digitCounts[l]
            if not numDigits:
                answers.append(0)
                continue
            
            moddedMultiplier = pow(10, numDigits, MOD)
            subsetConcat = (concats[r + 1] - ((concats[l]*moddedMultiplier) % MOD)) % MOD
            subsetSum = digitSums[r + 1] - digitSums[l]
            answers.append((subsetConcat * subsetSum) % MOD)


        return answers
