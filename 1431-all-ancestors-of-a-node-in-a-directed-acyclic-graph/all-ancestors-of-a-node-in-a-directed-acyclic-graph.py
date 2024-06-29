class Solution:
    def solveAncestorsForChild(self, solution, parents, solved, ind):
        if solved[ind]: return

        for parent in parents[ind]:
            solution[ind].add(parent)
            if not solved[parent]:
                self.solveAncestorsForChild(solution, parents, solved, parent)
            for ancestor in solution[parent]:
                solution[ind].add(ancestor)
        solved[ind] = True

        

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        solution = [set() for i in range(n)]
        parents = [[] for i in range(n)]

        for par, child in edges:
            parents[child].append(par)
        
        solved = [False for i in range(n)]
        for ind in range(n):
            self.solveAncestorsForChild(solution, parents, solved, ind)
        
        submission = [sorted(solution[ind]) for ind in range(n)]
        return submission


        