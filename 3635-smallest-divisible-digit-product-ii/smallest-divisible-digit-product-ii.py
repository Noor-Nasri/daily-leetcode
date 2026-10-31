class Solution:
    # This question is a bane of my existance but I will solve it with passion
    # So last month I got to the solution of handling edge cases and working one digit at a time
    # When we believe the next digit desired is not valid, we abort and increase value then put rest optiminally 

    # The problem arises when you actually need to lower the value, meaning you need to raise a prev value.
    # My old self thought this was an edge case to backtrack, but I think this overcomplicates it
    # What we really need is to change the condition for accepting the digit
    # Not only do we need to have enough digits left, but that count needs to START on the first val where max(factors) > val 
    
    # Issue is maybe on the way to the val, there is a 4 and a 2 to remove the 8, giving us an extra space. 
    # Instead: Can we try to end early at *every* ind, then once we can't, we take the last working sol?
    # Yes, this is the real trick

    def smallestPermute(self, factors):
        # factors is the correct num of digits, but we may be able to replace 3 with 2
        if factors[3] and factors[4]:
            factors[3] -= 1
            factors[4] -= 1
            factors[2] += 1
            factors[6] += 1

        result = []
        for i in range(10):
            for _ in range(factors[i]):
                result.append(str(i))
        return "".join(result)


    def newFactorsAfterVal(self, requiredFactors, newValue):
        # Alters the remaining factors to account for newValue, prioritizing smallest number of factors left.
        # We break the new value down to its factors (eg 8 -> 2,2,2) 
        # Then use each factor to either remove a value, or break a larger one down to make it easier to reduce later.

        remainingFactors = requiredFactors[::]
        breakdown = [
            [], [], [2], [3], [2, 2], [5], [2, 3], [7], [2, 2, 2], [3, 3]
        ]
        for newFactor in breakdown[newValue]:
            for oldFactor in range(2, 10):
                if not remainingFactors[oldFactor]:
                    continue

                if newFactor == oldFactor:
                    remainingFactors[newFactor] -= 1
                    break 
                elif oldFactor % newFactor == 0:
                    # The factor we need is divisible by the val we are adding -> Make the factor easier
                    remainingFactors[oldFactor] -= 1
                    remainingFactors[oldFactor // newFactor] += 1
                    break
        
        # We combine the broken (2, 3) back to (6) to save digits. 
        if remainingFactors[2] and remainingFactors[3]:
            remainingFactors[2] -= 1
            remainingFactors[3] -= 1
            remainingFactors[6] += 1

        return remainingFactors

    
    def smallestNumber(self, num: str, t: int) -> str:
        # Get factors and address 2 edge cases: Impossible t, and small num
        factors = [0 for i in range(10)]
        for factor in range(9, 1, -1):
            while t % factor == 0:
                factors[factor] += 1
                t //= factor

        # Edge case 1: Impossible to factorize with single digits
        if t != 1:
            return "-1"
        
        # Edge case 2: Small num, just put factors together
        #print(factors)
        numDigits = sum(factors) 
        if numDigits > len(num):
            return self.smallestPermute(factors)

        # Now for the general case: factored t and way too many digits in num
        bestSolution = None # (ind to change, new val, remaining factors)
        originalFactors = factors[::]
        for ind in range(len(num)):
            remainingRoom = len(num) - ind - 1
            val = int(num[ind])
            #print("Considering value", val)

            # First, consider if increasing this val can give a solution
            for newVal in range(val + 1, 10):
                newFactors = self.newFactorsAfterVal(factors, newVal)
                if sum(newFactors) <= remainingRoom:
                    bestSolution = (ind, newVal, newFactors)
                    #print("Solution still valid:", bestSolution)
                    break


            # If we see 0, we cant keep equality. Otherwise, keep trying
            # Unless 0, we will try to match to the very last ind
            if val == 0:
                break

            factors = self.newFactorsAfterVal(factors, val)
            #print(ind, "with val", val, "reduces factors to", factors)

            if ind == len(num) - 1 and sum(factors) == 0:
                # Edge case 3: we actually never needed to increase, num is valid
                return num

        if bestSolution == None: 
            # Edge case 4: Enough digits, but nothing can be increased properly. Add a digit. 
            remainingSuffix = self.smallestPermute(originalFactors)
            fillerLength = len(num) + 1 - len(remainingSuffix)
            return "1"*fillerLength + remainingSuffix
        
        firstIndChanged, newVal, remainingFactors = bestSolution
        remainingSuffix = self.smallestPermute(remainingFactors)
        fillerLength = len(num) - (firstIndChanged + 1) - len(remainingSuffix)
        return num[:firstIndChanged] + str(newVal) + "1"*fillerLength + remainingSuffix