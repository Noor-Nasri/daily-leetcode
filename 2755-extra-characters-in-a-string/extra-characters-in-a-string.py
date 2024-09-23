class Solution:
    def solve(self, ind):
        if ind in self.sols:
            return self.sols[ind]
        if ind == len(self.s): return 0

        options = [ self.solve(ind + 1) + 1 ]
        for choice in self.choices[ind]:
            options.append(self.solve(choice))
        
        self.sols[ind] = min(options)
        return self.sols[ind] 


    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        choices = [[] for i in range(len(s))] #index of where we can end up by taking a word in dict
        
        for word in dictionary:
            lastFound = 0
            while True:
                ind = s.find(word, lastFound)
                if ind == -1: break
                choices[ind].append(ind + len(word))
                lastFound = ind + 1
        

        self.choices = choices
        self.sols = {}
        self.s = s
        return self.solve(0)
