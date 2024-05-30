class Solution:
    def generate(self, string, rem_open, req_closed):
        if rem_open == 0 and req_closed == 1:
            return [string + ")"]

        # Choose to either close an open one, or open a new one
        solutions = []
        if req_closed > 0:
            sols = self.generate(string + ")", rem_open, req_closed - 1)
            solutions += sols
        
        if rem_open > 0:
            sols = self.generate(string + "(", rem_open - 1, req_closed + 1)
            solutions += sols
        
        #print("Solutions at", rem_open, req_closed, solutions)
        return solutions
        
        

    def generateParenthesis(self, n: int) -> List[str]:
        solutions = self.generate("(", n - 1, 1)
        
        # Because question wnats strict ordering, we sort
        return sorted(set(solutions))
                


        