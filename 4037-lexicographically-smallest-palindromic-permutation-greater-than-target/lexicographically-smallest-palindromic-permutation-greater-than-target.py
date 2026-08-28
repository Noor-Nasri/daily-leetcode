class Solution:
    # Okay so yesterday we just did two sweeps to figure it out, where we matched for as long as possible
    # The only change is palindrome, so can't we just do the same but only take pairs of chars?
    
    def createSmallest(self, availableCounts):
        chosen = []
        middleElement = ""
        for val in range(26):
            char = chr(val + 97)
            for i in range(availableCounts[val] // 2):
                chosen.append(char)
            
            if availableCounts[val] % 2:
                if middleElement:
                    return None
                else:
                    middleElement = char
        
        return "".join(chosen) + middleElement + "".join(chosen[::-1])



    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        if len(s) <= 1:
            if s > target:
                return s
            return ""

        # Setup input char counts and reduce them as we match s for as far as possible
        availableCounts = [0 for i in range(26)]
        ordA = ord('a')
        for char in s:
            availableCounts[ord(char) - ordA] += 1
            
        
        #print(availableCounts)
        indCutoff = (len(s) + 1) // 2 - 1 # 4 elements -> match till [1], 5 elements -> [2]
        for matchingInd in range(indCutoff + 1):
            isMiddleInd = matchingInd == (len(s) - 1) / 2
            val = ord(target[matchingInd]) - ordA
            if availableCounts[val] >= 2 or (isMiddleInd and availableCounts[val]):
               availableCounts[val] -= (isMiddleInd and 1 or 2)
            else:
                break
        else:
            matchingInd += 1 # We want matchingInd + 1 to be the first ind we did NOT match
        
        if matchingInd > indCutoff:
            # We can copy the first half fully - does this actually already go > target due to copied second half?
            
            isMiddleInd = indCutoff == (len(s) - 1)  / 2
            middle = target[indCutoff]*(isMiddleInd and 1 or 2)
            possible = target[:indCutoff] + middle + target[:indCutoff][::-1]
            if possible > target:
                return possible

        #print("Can match:", target[:matchingInd])

        # Now work backwards: first valid val we find is the latest ind we can divurge, so closest
        for ind in range(min(indCutoff, matchingInd), -1, -1):
            initVal = ord(target[ind]) - ordA
            isMiddleInd = ind == (len(s) - 1)  / 2
            if ind < matchingInd: # re-include because we are about to change it
                availableCounts[initVal] += (isMiddleInd and 1 or 2)

            #print("Now looking for ind:", ind, isMiddleInd,  "with remaining options:", availableCounts)

            # Now try all larger chars in order
            for val in range(initVal + 1, 26):
                if availableCounts[val] >= 2 or (isMiddleInd and availableCounts[val]):
                    char = chr(val + ordA) 
                    if isMiddleInd:
                        return target[:ind] + char + target[:ind][::-1]

                    availableCounts[val] -= 2
                    middlePermute = self.createSmallest(availableCounts)
                    if middlePermute != None:
                        return target[:ind] + char + middlePermute + char + target[:ind][::-1]
                    
                    availableCounts[val] += 2

        return ""