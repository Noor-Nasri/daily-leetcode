
class Solution:
    def complexSolver(self, start, end, solved):
        # 100 * 100 * 26
        if (start, end, solved) in self.sols:
            return self.sols[(start, end, solved)]
        
        if start >= end or start >= len(self.s):
            return 0
        

        relevantChar = self.s[start]

        
        best = 10000000
        if relevantChar == solved:
            best = self.complexSolver(start + 1, end, solved)
        
        elif relevantChar == self.s[end - 1]:
            # Greedy closing boundary
            best = 1 + self.complexSolver(start + 1, end - 1, relevantChar)
        
        else:

            for possible_end in range(start, end):
                if relevantChar != self.s[possible_end]: continue

                # we can possibly make this adjustment
                cost_inside = self.complexSolver(start + 1, possible_end, relevantChar)
                cost_outside = self.complexSolver(possible_end + 1, end, solved)
                best = min(best, 1 + cost_inside + cost_outside)

        self.sols[(start, end, solved)] = best
        return best


    def strangePrinter(self, s: str) -> int:
        self.sols = {}
        self.s = s
        return self.complexSolver(0, len(s), '')
        
        