class Solution:
    # This is a messy solution, but we only need to run it once and store 20 results
    # There is no 'clean' solution here, as we need to do backtracking anyways. 
    # Only need to make our stops smart enough to run for n in [1, 20]

    def solveInOrder(self, curValues):
        if self.firstSol != None:
            return

        if 0 not in curValues:
            self.firstSol = curValues
            return

        usedValues = set(curValues)
        ind = curValues.index(0)
        for i in range(self.n, 0, -1):
            if i in usedValues:
                continue
            
            if i == 1:
                curValues[ind] = 1
                self.solveInOrder(curValues)
                continue
            
            if ind + i >= len(curValues) or curValues[ind + i]:
                continue
            
            next_vals = curValues[:]
            next_vals[ind] = i
            next_vals[ind + i] = i
            self.solveInOrder(next_vals)


    def constructDistancedSequence(self, n: int) -> List[int]:
        self.n = n
        self.firstSol = None 
        self.solveInOrder([0 for i in range(2 * n - 1)])
        return self.firstSol
        