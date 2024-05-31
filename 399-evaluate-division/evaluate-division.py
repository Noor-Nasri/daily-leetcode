class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        divisions = {}

        def found(num, denom, val):
            if denom in divisions[num]: return # already done

            # Known already
            divisions[num][denom] = val
            if num == denom: return # cant get anything out of x/x=1
            if val != 0: divisions[denom][num] = 1/val
            
            # Get info by eliminating denom
            oldDenoms = list(divisions[denom].keys())
            for newDenom in oldDenoms:
                newVal = val * divisions[denom][newDenom]
                found(num, newDenom, newVal)

            # Get info by eliminating num
            oldNums = list(divisions[num].keys())
            for newNum in oldNums:
                if divisions[num][newNum] == 0: continue
                newVal = val / divisions[num][newNum]
                found(newNum, denom, newVal)


        for ind in range(len(equations)):
            num, denom = equations[ind]
            val = values[ind]

            if not num in divisions: divisions[num] = {}
            if not denom in divisions: divisions[denom] = {}
            found(num, denom, val)

        answers = []
        for a, b in queries:
            if not a in divisions or not b in divisions[a]: 
                answers.append(-1.0)
            else:
                answers.append(divisions[a][b])
        
        return answers

                




        