
class Solution:
    def complexSolver(self, start, end, solved):
        # 100 * 100 * 26
        if (start, end, solved) in self.sols:
            return self.sols[(start, end, solved)]
        
        if start >= end or start >= len(self.s):
            return 0

        if solved[ord(self.s[start]) - ord('a')]:
            return self.complexSolver(start + 1, end, solved)

        best = 10000000

        for possible_end in range(start, end):
            if self.s[start] != self.s[possible_end]: continue

            # we can possibly make this adjustment
            solved_inside = [0 for i in range(26)]
            solved_inside[ord(self.s[start]) - ord('a')] = 1
            cost_inside = self.complexSolver(start + 1, possible_end, tuple(solved_inside))
            cost_outside = self.complexSolver(possible_end + 1, end, solved)
            best = min(best, 1 + cost_inside + cost_outside)

        self.sols[(start, end, solved)] = best
        return best


    def strangePrinter(self, s: str) -> int:
        self.sols = {}
        self.s = s
        return self.complexSolver(0, len(s), tuple(0 for i in range(26)))
        
        