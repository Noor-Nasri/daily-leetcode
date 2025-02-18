class Solution:
    def exploreBranches(self, numbers, pattern):
        if self.smallestAnswer != None:
            return
        
        if len(numbers) == len(pattern) + 1:
            self.smallestAnswer = "".join([str(e) for e in numbers])
            return
        
        increasing = pattern[len(numbers) - 1] == "I"
        smallestAllowed = increasing and numbers[-1] + 1 or 1
        biggestAllowed =  increasing and 9 or numbers[-1] - 1

        for nextNum in range(smallestAllowed, biggestAllowed + 1):
            if nextNum in numbers: continue 
            self.exploreBranches(numbers + [nextNum], pattern)


    def smallestNumber(self, pattern: str) -> str:
        self.smallestAnswer = None
        for i in range(1, 10):
            self.exploreBranches([i], pattern)
        
        return self.smallestAnswer