class Solution:
    def getAllCombinations(self, curInd, remTarg):
        # Ignore all the messiness .. I accidently excluded the memoization and ended up hyper optimizing
        if (curInd, remTarg) in self.sols:
            solution = []
            for lis in self.sols[(curInd, remTarg)]:
                solution.append(lis[::])
            return solution
             

        if curInd >= len(self.candidates) or self.remainingSums[curInd] < remTarg: return []

        ind_nextNum = curInd + 1
        while ind_nextNum < len(self.candidates) and self.candidates[curInd] == self.candidates[ind_nextNum]:
            ind_nextNum += 1
        combos_without_element = self.getAllCombinations(ind_nextNum, remTarg)
        combos_with_element = []

        if self.candidates[curInd] == remTarg:
            combos_with_element = [[remTarg]]

        elif self.candidates[curInd] < remTarg:
            combos_with_element = self.getAllCombinations(curInd + 1, remTarg - self.candidates[curInd])
            for comboInd in range(len(combos_with_element)):
                combos_with_element[comboInd].append(self.candidates[curInd])

        for combo_bonus in combos_with_element:
            combos_without_element.append(combo_bonus)
            
        self.sols[(curInd, remTarg)] = combos_without_element
        solution = []
        for lis in self.sols[(curInd, remTarg)]:
            solution.append(lis[::])
        return solution
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.sols = {}
        self.candidates = candidates
        self.remainingSums = [0 for i in range(len(candidates))]
        total = 0
        for ind in range(len(candidates) -1, -1, -1):
            total += candidates[ind]
            self.remainingSums[ind] = total


        allCombos = self.getAllCombinations(0, target)
        unique = set()
        results = []
        for ind in range(len(allCombos)):
            allCombos[ind] = sorted(allCombos[ind]) # for some reason it must be sorted ..
            ID = tuple(allCombos[ind])

            if not ID in unique:
                unique.add(ID)
                results.append(allCombos[ind])
        
        return results
        