class Solution:
    # Okay this looks intimidating. So, if we were to iterate like a stack and keep comparing the last two,
    # We need to evaluate the GCD and LCM quickly. This would be 10^5 * 2 * T(eval)
    # We might be able to pre-compute all the primes, then we say GCD by looping through the primes. 
    # Likewise the LCM could be a mash of their primes(?) But this whole thing can't be within bounds

    # Maybe it is within bounds. Lets track this more closely.
    # We can compute primes in O(max val), which is 10^5.
        # On top of detecting if a number is prime, we need to know the factorization of non-primes.
        # We can start by having every non-prime tracked as {prime: 1, otherPrime: 1}, then fill in the counts in O(n * numFactors). So 10^5 * like 20
    # If we manage to do this quickly, then we just simulate. GCD is done by comparing prime tables. LCM is done by merging them.
    
    def getFactorCount(self, num, primeFactor):
        c = -1
        while num % 1 == 0:
            num /= primeFactor
            c += 1

        return c
        
    def preComputeFactorTable(self, maxNum):
        nonPrimeToFactors = {}
        for num in range(2, maxNum + 1):
            if num in nonPrimeToFactors:
                continue
            
            # This number is a prime
            mult = 2
            while mult * num <= maxNum:
                val = mult * num
                factorCount = self.getFactorCount(val, num)
                if not val in nonPrimeToFactors:    
                    nonPrimeToFactors[val] = {}

                nonPrimeToFactors[val][num] = factorCount
                mult += 1

        return nonPrimeToFactors

    
    def areNumsNonCoPrimes(self, nonPrimeToFactors, num1, num2):
        #print(f"Checking ncp for {num1}, {num2}")
        # True when they are non-coprimes, meaning True iff GCD(num1, num2) > 1
        
        if num1 == 1 or num2 == 1:
            return False # edge case, 1 cant have GCD > 1
        elif num1 == num2:
            return True
        elif num1 not in nonPrimeToFactors or num2 not in nonPrimeToFactors:
            # One is a prime, so they are coprimes unless its a multiple
            ##print("One is prime, special case")
            return ((num1 % num2 == 0) or (num2 % num1 == 0))

        for primeFactor in nonPrimeToFactors[num1]:
            if primeFactor in nonPrimeToFactors[num2]:
                ##print(primeFactor, "is a > 1 factor")
                return True
        
        for primeFactor in nonPrimeToFactors[num2]:
            if primeFactor in nonPrimeToFactors[num1]:
                ##print(primeFactor, "is a > 1 factor")
                return True
        
        #print(f"{num1}, {num2} have GCD == 1")
        return False
    
    def solveLCM(self, nonPrimeToFactors, num1, num2):
        if num1 == num2:
            return num1, nonPrimeToFactors.get(num1)

        #print(f"Solving lcm for {num1}, {num2}")
        if num1 not in nonPrimeToFactors or num2 not in nonPrimeToFactors:
            # For them to reach here, one is prime, and the other is a multiple of the prime. 
            
            lcm = max(num1, num2)
            factors = nonPrimeToFactors[lcm]
            return lcm, factors

        factors = {}
        lcm = 1
        for primeFactor in nonPrimeToFactors[num1]:
            c1, c2 = nonPrimeToFactors[num1][primeFactor], nonPrimeToFactors[num2].get(primeFactor, 0)
            count = max(c1, c2)
            factors[primeFactor] = count
            lcm *= (primeFactor ** count)
        
        for primeFactor in nonPrimeToFactors[num2]:
            if primeFactor in factors:
                continue

            c1, c2 = nonPrimeToFactors[num2][primeFactor], nonPrimeToFactors[num1].get(primeFactor, 0)
            count = max(c1, c2)
            factors[primeFactor] = count
            lcm *= (primeFactor ** count)

        return lcm, factors

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        nonPrimeToFactors = self.preComputeFactorTable(max(nums))
        curList = []

        for v in nums:
            curList.append(v)

            while len(curList) >= 2 and self.areNumsNonCoPrimes(nonPrimeToFactors, curList[-1], curList[-2]):
                ncp1, ncp2 = curList.pop(), curList.pop()
                lcm, factors = self.solveLCM(nonPrimeToFactors, ncp1, ncp2)
                #print("Replacing", ncp1, ncp2, "with", lcm)
                if factors != None: # We dont factor primes
                    nonPrimeToFactors[lcm] = factors
                curList.append(lcm)
        
        return curList