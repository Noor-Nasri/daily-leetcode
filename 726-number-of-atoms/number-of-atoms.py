class Solution:
    def solveCount(self, formula, ind):
        ind2 = ind + 1
        while (ind2 < len(formula) and formula[ind2].isdigit()):
            ind2 += 1
        
        return (int(formula[ind:ind2]), ind2)
    
    def getFullSymbol(self, formula, ind):
        ind2 = ind + 1
        while (ind2 < len(formula) and 'a' <= formula[ind2] <= 'z'):
            ind2 += 1
        
        return (formula[ind:ind2], ind2)

    def insertSymbol(self, counts, element, count):
        if element in counts[-1]:
            counts[-1][element] += count
        else:
            counts[-1][element] = count
    
    def countOfAtoms(self, formula: str) -> str:
        chained_counted = [{}] # stack of totals for parathesis 
        cur_ind = 0

        while (cur_ind < len(formula)):
            if formula[cur_ind] == "(":
                chained_counted.append({})
                next_ind = cur_ind + 1

            elif formula[cur_ind] == ")":
                multiplier, next_ind = (1, cur_ind + 1)
                if next_ind < len(formula) and formula[next_ind].isdigit():
                    multiplier, next_ind = self.solveCount(formula, next_ind)
                
                cur_counts = chained_counted.pop()
                for element in cur_counts:
                    self.insertSymbol(chained_counted, element, cur_counts[element] * multiplier)
            
            else: # New symbol
                symbol, next_ind = self.getFullSymbol(formula, cur_ind)
                multiplier = 1
                if next_ind < len(formula) and formula[next_ind].isdigit():
                    multiplier, next_ind = self.solveCount(formula, next_ind)
                self.insertSymbol(chained_counted, symbol, multiplier)
            
            cur_ind = next_ind

        final = []
        for key in sorted(chained_counted[0]):
            final.append(key)
            occurances = chained_counted[0][key]
            if occurances > 1: final.append(str(occurances))
                
        return "".join(final)
        
        