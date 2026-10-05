class Solution:
    # If it's exactly equal, it's simple: 2 pointer solution to match word2 while sweeping word1.
    # Can we maybe pre-emptively compute the earliest valid solution until each ind in word2?
    # The precompute is easy, but this still does n^2 after to consider each ind in word2...
    # BS wont work: If we know ignoring [4] doesnt work, we dont know if ignoring [2] might have actually helped.
    # DP wont work: We can't avoid segregating ind1 by the chosen replacement of current ind.
    # How do we solve this without n^2???

    # Can we do some form of 2p where we take the first 'trick' we can, but store the alternative as we go?
    # We would keep the greedy one until we get stuck, then we go through the queue of alternatives.. 
    # We would somehow maintain the 'best' queue, with a stack of edits to the 'original', ie unedited queue. 

    # Okay, I think that might work but I can't prove its not n^2. So the idea is:
    # Store {needed_char: [(option, curInd)]}. Eg (orig, 2) -> are looking to match [2], no swaps yet
    # Every time we match orig, we spin up one more option for immediately ignoring next ind.
    # HOWEVER: Once options meet back at the same required ind, we can combine them.

    # So each ind: lookup char -> iterate on existing options, merge into earliest or orig.
    # Like, if replacing [1] gets stuck looking for [2], original is also stuck and no options are generated.
    # When [2] is found, it puts both together and we can stop tracking this option - it is valid if orig is valid.
    # We only expand when [1] finds [2] early, now its tracking for [3] while orig seeking [1].
    # When orig finally finds [1], it creates [2] seeking [3]. BUT: since [1] is already tracking [3] EARLIER, we throw away [2]!
    # Yes, I think this is indeed O(n). It should work. Just need to track two paths.

    def attemptDirectSolve(self, word1, word2):
        # Switches the first possible ind and tries to match the full words
        chosenInds = []
        for ind in range(len(word2)):
            chosenInds.append(ind)
            if word1[ind] != word2[ind]:
                break
        
        if len(chosenInds) == len(word2):
            return chosenInds
        
        for ind in range(chosenInds[-1] + 1, len(word1)):
            charFound = word1[ind]
            charNeeded = word2[len(chosenInds)]

            if charFound == charNeeded:
                chosenInds.append(ind)
                
                if len(chosenInds) == len(word2):
                    return chosenInds
        
        return []

    def validSequence(self, word1: str, word2: str) -> List[int]:
        directSolution = self.attemptDirectSolve(word1, word2)
        if directSolution:
            return directSolution

        # No direct solution exists, so we will try all viable shifts
        mainPath = []
        altPath = [0]
        altPathSplitInd = 0

        for ind in range(len(word1)):
            char = word1[ind]
            altCharInd = altPathSplitInd + len(altPath)

            if ind > altPath[-1] and altCharInd < len(word2) and char == word2[altCharInd]:
                altPath.append(ind)
            
            if char == word2[len(mainPath)]:
                mainPath.append(ind)
                if len(mainPath) == altPathSplitInd + len(altPath):
                    # Continuing this path is now the same as following the main path, which fails
                    # Spin up a new alt path that follows main path until the next one
                    altPath = [ind + 1]
                    altPathSplitInd = len(mainPath)
        
        if altPathSplitInd + len(altPath) == len(word2):
            return mainPath[:altPathSplitInd] + altPath
        else:
            return []


            
            
        