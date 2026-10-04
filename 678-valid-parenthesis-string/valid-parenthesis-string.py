class Solution:
    # So without * this becomes a simple counter.
    # Can we just sweep and ignore * until it breaks?
    # For example: if we run into an extra ), we can turn the last * into an open (
    # On the other hand, if we finish and we still have opened brackets, can we close them?
    # That is more tricky, because adding a ) can break it. Eg: *(. 'Fixing' makes it )(.

    # So the general rule is: if we are going to add a closed ), it should always be at the end.
    # Given constraints, an ugly but working solution is: Try [1->100] closed brackets. Set them. then sweep.

    def checkValidString(self, s: str) -> bool:
        totalFree = s.count('*')
        for numForcedClosed in range(totalFree + 1):
            curOpen = 0
            curFree = 0
            remainingFree = totalFree - numForcedClosed
            viable = True

            for c in s:
                if c == "*" and remainingFree:
                    remainingFree -= 1
                    curFree += 1
                elif c == ")" or c == "*":
                    # Must be closed
                    if curOpen:
                        curOpen -= 1
                    elif curFree:
                        curFree -= 1
                    else:
                        viable = False
                        break
                else:
                    curOpen += 1


            if viable and curOpen == 0:
                return True

        return False