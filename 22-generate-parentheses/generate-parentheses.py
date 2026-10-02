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
        
        return solutions
    
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = self.generate("(", n - 1, 1)
        return sorted(set(solutions))
                


        