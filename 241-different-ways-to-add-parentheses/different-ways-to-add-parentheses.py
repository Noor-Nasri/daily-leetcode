class Solution:
    def getMaxValidCloses(self, openBrackets):
        for ind in range(len(openBrackets) - 1, 0, -1):
            if openBrackets[ind] == openBrackets[ind - 1]:
                return len(openBrackets) - ind

        return len(openBrackets)

    def exploreAllBranches(self, ind, remainingBrackets, openBrackets, stringSoFar):
        # before each number, we add [0, x] brackets
        # when we choose 0 (openBrackets must be > 0), we then close [1, openbrackets]
        if ind == len(self.expr) - 1:
            # finished
            if remainingBrackets: return
            if self.getMaxValidCloses(openBrackets) != len(openBrackets):
                return

            stringSoFar += self.expr[-1] + ")"*len(openBrackets)
            self.ans.append(eval(stringSoFar))
            return
        
        # option 1: close existing brackets
        bracketCopy = openBrackets[:]
        for numClosingBrackets in range(1, self.getMaxValidCloses(openBrackets) + 1):
            bracketCopy.pop()

            self.exploreAllBranches(
                ind + 2, remainingBrackets, bracketCopy[:], 
                stringSoFar + self.expr[ind] + ")"*numClosingBrackets + self.expr[ind + 1]
                )


        # option 2: open new brackets
        bracketCopy = openBrackets[:]
        for numNewBrackets in range(1, remainingBrackets + 1):
            bracketCopy.append(ind)
            self.exploreAllBranches(
                ind + 2, remainingBrackets - numNewBrackets, bracketCopy[:], 
                stringSoFar +  "(" * numNewBrackets + self.expr[ind] + self.expr[ind + 1]
                )



    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.ans = []
        self.expr = []

        self.specials = {"+", "-", "*"}
        char_ind = 0
        while char_ind < len(expression):
            if expression[char_ind] in self.specials:
                self.expr.append(expression[char_ind])
            elif char_ind == len(expression) - 1 or expression[char_ind + 1] in self.specials:
                self.expr.append(expression[char_ind])
            else:
                self.expr.append(expression[char_ind:char_ind+2])
                char_ind += 1
            char_ind += 1
        
        if len(self.expr) == 1:
            return [int(self.expr[0])]
        
        numBrackets = (len(self.expr) - 1) // 2
        self.exploreAllBranches(0, numBrackets,  [], "")
        return self.ans
