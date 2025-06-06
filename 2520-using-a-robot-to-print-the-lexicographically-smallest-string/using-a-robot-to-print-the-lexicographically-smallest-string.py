class Solution:
    def robotWithString(self, s: str) -> str:
        # We have a choice:
        # (1) pop last element
        # (2) go all the way forward to the smallest element, so that we can put that first
        # We should keep doing (2) until we realize that last element is <= the smallest further out
        # <--> Simplified: Just add to stack and pop the top when it beats the remaining elements
        remainingCounts = [0 for i in range(26)]
        for c in s:
            remainingCounts[ord(c) - 97] += 1
        
        bestRemainingInd = 0
        finalString = []
        curStack = []
        for c in s:
            c_ind = ord(c) - 97
            curStack.append(c_ind)
            remainingCounts[c_ind] -= 1 

            while bestRemainingInd < len(remainingCounts) and remainingCounts[bestRemainingInd] == 0:
                bestRemainingInd += 1

            while curStack and curStack[-1] <= bestRemainingInd:
                newChar = chr(curStack.pop() + 97)
                finalString.append(newChar)
        
        return "".join(finalString)
        