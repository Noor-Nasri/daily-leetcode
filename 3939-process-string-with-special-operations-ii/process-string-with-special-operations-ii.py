class Solution:
    # The medium version just has s <= 20 so we did a basic stack, ie 2^s
    # This hard version isn't asking for the full string anymore, so we can be smarter

    # The trick is going to be to narrow down the chain of operations that impact ind x
    # First get all the operations in order and know the total # of chars, then solve backwards
    # Imagine we first pop a letter. That is our return if we wanted ind s - 1.
    # If it's #, then we know the remaining length can be halved, and we shift k 
    # If its %, then we can flip k on the remaining portion.
    # What about *? How about we consider k as "dist from end", then we just add one here
    # So dont actually remove the letter, just shift our target one over.
    # Actually, better yet: Work towards ind k and keep # of pending removals
    
    # This means we can pop one operation at a time, ie 10^5, and not actually build anything
    def processStr(self, s: str, k: int) -> str:
        commands = []
        totalLength = 0
        for c in s:
            commands.append(c)
            if c == "*":
                totalLength = max(0, totalLength - 1)
            elif c == "#":
                totalLength *= 2
            elif c != "%":
                totalLength += 1
        
        if k >= totalLength:
            return "."
        
        #print("Total length of final string is", totalLength)
        nextCharInd = totalLength - 1
        desiredInd = k
        pendingRemovals = 0
        while commands:
            lastOperation = commands.pop()
            #print("-----")
            #print("Now inspecting:", lastOperation)
            if lastOperation == "*":
                pendingRemovals += 1
            elif lastOperation == "#":
                originalHalfLen = (nextCharInd + 1 + pendingRemovals) // 2
                if desiredInd < originalHalfLen:
                    # Take first half, so just throw away the duplicate
                    pendingRemovals = max(0, pendingRemovals - originalHalfLen)
                else:
                    # Take second half, so still appoly removals but shift target
                    desiredInd -= originalHalfLen
                nextCharInd = originalHalfLen - 1 - pendingRemovals

            elif lastOperation == "%":
                desiredInd = (nextCharInd + pendingRemovals) - desiredInd
                nextCharInd += pendingRemovals
                pendingRemovals = 0 # We flipped which ind we actually want
                # This essentially means going back to before the flip and changing k
                # The items that were pending removal are always going to be after desiredInd
                # So in the original they are before the desiredInd
                # So we can just forget about removing them because we'll never reach them
            elif pendingRemovals:
                pendingRemovals -= 1 # Ignore this char
            elif nextCharInd == desiredInd:
                return lastOperation
            else:
                nextCharInd -= 1
            
            ##print(f"desiredInd = {desiredInd}, nextCharInd= {nextCharInd}, pendingRemovals= {pendingRemovals}")

        return "."








