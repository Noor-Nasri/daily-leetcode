class Solution:
    # We need to precompute the divisors for the first 10^5 numbers, then apply it to the list
    # We can do this by having each number add to future number lists, and if a number has 2 factors already it doesnt bother
    # Will this tle? Hard to count .. 10^5 * (num elements with <= 4 factors)

    def __init__(self):
        factorLists = [[1, i] for i in range(10**5 + 1)]
        
        for num in range(2, 10**5 + 1):
            if len(factorLists[num]) > 4:
                continue
            
            mult = num * 2
            while mult <= 10**5:
                factorLists[mult].append(num)
                mult += num
        
        self.sumValues = [len(e) == 4 and sum(e) or 0 for e in factorLists]


    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += self.sumValues[num]
        return total 