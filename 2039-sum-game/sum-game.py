class Solution:
    # Okay, so we can boil this down to a starting diff, and a number of turns for each side
    # This feels like DP, minimax, or a simple greedy. Need to think through the game
    # Okay, SO: If Alice goes last, she'll always win by making unequal
    # Once down to only one side we have (Diff, numTurns):
    # If diff < numTurns * 9: Alice wins by just adds 9 every turn. 
    # If diff > numTurns * 9: Alice wins by just not helping.
    
    # Bob needs to somehow get the Diff to exactly 9x before a side is finished
    # Alice knows this. So if the starting Diff is > 9x, she just always puts 9 and wins
    # If Diff == 9*x, Bob can always counteract Alice by placing an equal amount on the other side 
    # If Diff < 9*x, it means we need to increase the larger side - so they can just put 9 on smaller

    # SO: Bob can win ONLY iff:
    # - There is an even number of slots
    # - numSlots on the side with smaller sum is >= numSlots on the bigger side
    # - 9 * (slotDiff/2) == initial diff.

    def sumGame(self, num: str) -> bool:
        totals = [0, 0]
        numSlots = [0, 0]
        cutoff =  len(num)//2
        for ind in range(len(num)):
            arrInd = int(ind >= cutoff)
            if num[ind] == '?':
                numSlots[arrInd] += 1
            else:
                totals[arrInd] += int(num[ind])

        #print(totals, numSlots)
        
        if sum(numSlots) % 2 == 1:
            return True

        # Flip totals[0] to be the smaller one
        if totals[0] > totals[1]:
            totals = totals[::-1]
            numSlots = numSlots[::-1]
        
        if totals[0] < totals[1] and numSlots[0] < numSlots[1]:
            return True
        
        initDiff = totals[1] - totals[0]
        turnsToFix = (max(numSlots) - min(numSlots)) // 2
        #print(initDiff, turnsToFix)
        return initDiff != turnsToFix * 9 