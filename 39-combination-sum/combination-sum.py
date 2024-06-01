class Solution:
    def helper(self, candidates, target, ind):
        if target == 0: return [[]]
        if ind == len(candidates) or target < 0: return False
        if (ind, target) in self.sols: 
            return self.sols[(ind, target)]

        #print(target, ind)
        num = candidates[ind]
        max_buy = target // num

        all_solutions = []
        for amount in range(max_buy + 1):
            solutions = self.helper(candidates, target - num * amount, ind + 1)
            if not solutions: continue
            #print("In order to solve", target, "at", ind, "we asked for", target - num * amount)
            for sol in solutions:
                new_sol = sol[:]
                for j in range(amount):
                    new_sol.append(num)
                all_solutions.append(new_sol)

        self.sols[(ind, target)] = all_solutions
        #print("Found all sol to", target, "at", ind, all_solutions)
        return self.sols[(ind, target)]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.sols = {}
        return self.helper(candidates, target, 0)
        