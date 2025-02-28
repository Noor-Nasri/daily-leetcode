class Solution:
    def minLenToComplete(self, ind1, ind2):
        if ind1 == len(self.str1) and ind2 == len(self.str2):
            return 0
        
        if (ind1, ind2) in self.sols:
            return self.sols[(ind1, ind2)]
        
        sol = None
        if ind1 == len(self.str1):
            sol = 1 + self.minLenToComplete(ind1, ind2 + 1)
        elif ind2 == len(self.str2):
            sol = 1 + self.minLenToComplete(ind1 + 1, ind2)
        elif self.str1[ind1] == self.str2[ind2]:
            sol = 1 + self.minLenToComplete(ind1 + 1, ind2 + 1)
        else:
            sol = min(
                1 + self.minLenToComplete(ind1 + 1, ind2),
                1 + self.minLenToComplete(ind1, ind2 + 1),
            )
        
        self.sols[(ind1, ind2)] = sol
        return sol
    
    def extractBestSolution(self):
        curString = []
        options = [self.str1, self.str2]
        curInds = [0, 0]

        while curInds[0] < len(options[0]) or curInds[1] < len(options[1]):
            #print("Currently at", curString, curInds)
            decision = None
            if curInds[0] == len(options[0]) or curInds[1] == len(options[1]):
                decision = int(curInds[0] == len(options[0]))
                #print("Forced to take", decision)

            elif options[0][curInds[0]] == options[1][curInds[1]]:
                curString.append(options[0][curInds[0]])
                curInds[0] += 1
                curInds[1] += 1
                #print("Match!")
                continue
            else:
                op2IsShorter = self.sols[(curInds[0], curInds[1] + 1)] < self.sols[(curInds[0] + 1, curInds[1])]
                decision = int(op2IsShorter)
                #print("Choose to take", decision)

            curString.append(options[decision][curInds[decision]])
            curInds[decision] += 1


        return "".join(curString)

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        self.sols = {}
        self.str1 = str1
        self.str2 = str2
        self.minLenToComplete(0, 0)
        #print(self.sols)
        return self.extractBestSolution()