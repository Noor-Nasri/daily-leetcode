class Solution:
    # This is interesting, lets split into (1) solve min #, then (2) get all combos of #
    # If we know the count, then its a basic DP: (ind, numOpen, numMissing) -> n is tiny, no problem.

    # So the real question is, whats the *maximum* number of parantheses we can include?
    # Do we need BS for this, or can we just do another basic DP?
    # (ind, numOpen) -> Returns min removals needed to finish. Seems simple

    def solveMinRemovals(self, ind, curOpen):
        uid = (ind, curOpen)
        if curOpen < 0:
            return None

        if ind == len(self.s):
            if curOpen:
                return None
            else:
                return 0
        
        if uid in self.sols:
            return self.sols[uid]
        
        options = []
        inclusionImpact = self.mapping.get(self.s[ind], 0)
        op_keep = self.solveMinRemovals(ind + 1, curOpen + inclusionImpact)
        if op_keep != None:
            options.append(op_keep)

        if inclusionImpact:
            op_ignore = self.solveMinRemovals(ind + 1, curOpen)
            if op_ignore != None:
                options.append(1 + op_ignore)
        
        if options:
            sol = min(options)
        else:
            sol = None
        
        self.sols[uid] = sol
        return sol
    
    def createAllPermutes(self, ind, curOpen, numToOpen, inclusionStack):
        # We can do dp but I think we can just brute force it once we know expected length
        # curOpen, numToOpen <= 10. ind, inclusionStack <= 25. List creation inside 25. is enough.
        if ind == len(self.s):
            if not curOpen and not numToOpen:
                self.allOptions.add("".join(inclusionStack))
            return

        if self.s[ind] == "(":
            self.createAllPermutes(ind + 1, curOpen, numToOpen, inclusionStack)
            if numToOpen:
                self.createAllPermutes(ind + 1, curOpen + 1, numToOpen - 1, inclusionStack + ['('])
            
        elif self.s[ind] == ")":
            self.createAllPermutes(ind + 1, curOpen, numToOpen, inclusionStack)
            if curOpen:
                self.createAllPermutes(ind + 1, curOpen - 1, numToOpen, inclusionStack + [')'])
        else:
            self.createAllPermutes(ind + 1, curOpen, numToOpen, inclusionStack + [self.s[ind]])



    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.mapping = {'(' : 1, ')': -1}
        self.sols = {}
        self.s = s

        openCount = s.count("(")
        closedCount = s.count(")")
        minRemovals = self.solveMinRemovals(0, 0)
        forcedRemovals = max(openCount, closedCount) - min(openCount, closedCount)
        numOpenBrackets = min(openCount, closedCount) - (minRemovals - forcedRemovals)//2
        self.allOptions = set()
        self.createAllPermutes(0, 0, numOpenBrackets, [])
        return list(self.allOptions)



