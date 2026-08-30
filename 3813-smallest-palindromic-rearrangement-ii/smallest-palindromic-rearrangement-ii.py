class Solution:
    # I think we can actually just reduce this to a non palindrome question:
    # Based on the counts, we can arrange the first half as desired and rest is forced

    # If we can somehow form DP (ind) -> # unique, it would be trivial sweep.
    # There has to be some recurrence. If we select ind0='a' does ind1 NEED to know a was chosen?
    # If it just picks n-1 elements elements and removes a 'z' instead, well wheverer it puts the a, pretend its a z
    # What if there are (a=2, z=1)? (1, 1) means two combos left: az, za. But (2, 0) only has aa.

    # BUT we can squueze in O(s^2) because we cut to s/2, so total is 25mil. Limit probably 30mil.
    # OKay, one other constraint: there is like 26^n combos but k <= 10^6.
    # SO: Maybe we just brute force it with early aborts!

    # Like why can't we literally just start with lowest palindrome, and go 1 higher until k??
    # Aint no way I spent a month pondering this when the constraint allows brute force!
    
    # Okay, I think this is the trick: Start with lowest palindrome, then go to n-2
    # Say lowest has n-2=y, n-1=z. Now you push to zy, which skips (1) permute. [n-2] now represents (2) options
    # Now say n-3=x. So now trying y, z each skips (2) options. [n-3] represents (6) options.
    # Keep working backwards until ind=x picks the correct value.
    
    # We can just do n^2 here by redoing the backward sweep on remaining
    # There is probably an optimization here with shifting the chars properly and just forward sweeping

    def chooseNextChar(self, curChar, availableChars, curCombinations, k):
        # Returns (replacement, numSkipped). replacement == 0 means we can't reach k yet.
        # If replacement > 0, we select and can solve k_next = (k-numSkipped)

        numSkipped = curCombinations
        for replacement in range(curChar + 1, 26):
            if not availableChars[replacement]:
                continue
            
            # Given the initial char, curCombinations = nCk1 * (n-k1)Ck2 * (n-k1 - k2)Ck3 * ...
            # Say k1 = #curChar, k2 = #replacement and we now change curChar -> replacement
            # nCk1 becomes nC(k1 + 1) cuz one more free curChar --> Multiply by (n-k1)/(k1+1) to fix
            # n2Ck2 becomes (n2-1)C(k2-1) --> Multiply by k2/n2 = k2/(n-k1) to fix
            # THEREFORE: number of combs shifts by multiple of #replacement/(#orig + 1)
            
            selectionCombos = curCombinations * availableChars[replacement] / (availableChars[curChar] + 1)
            if numSkipped + selectionCombos >= k:
                return (replacement, numSkipped)
            
            numSkipped += selectionCombos

        return (0, numSkipped)
    
    def solveRemaining(self, counts, k, finalArr):
        # Solves earliest ind that changes, then calls recursively for the rest
        #print("====== Solving for ", counts, "with k=", k, "and locked=", finalArr)
        smallestPermute = []
        for val in range(26):
            for _ in range(counts[val]):
                smallestPermute.append(val)
        
        if not smallestPermute:
            return 
        elif k == 1:
            for chosenChar in smallestPermute:
                finalArr.append(chr(chosenChar + 97))
            return 


        # Now setup the sweep from n-1
        availableChars = [0 for i in range(26)]
        availableChars[smallestPermute[-1]] += 1
        curCombinations = 1

        for indBackward in range(len(smallestPermute) - 2, -1, -1):
            curChar = smallestPermute[indBackward]
            chosenChar, curCombinations = self.chooseNextChar(curChar, availableChars, curCombinations, k)
            availableChars[curChar] += 1

            if chosenChar:
                #print("Chosen:", chosenChar, "which skips", curCombinations, "combinations")
                # Lock in until this char
                for indLocked in range(indBackward):
                    finalArr.append(chr(smallestPermute[indLocked] + 97))
                finalArr.append(chr(chosenChar + 97))
                availableChars[chosenChar] -= 1

                return self.solveRemaining(availableChars, k - curCombinations, finalArr)


    def smallestPalindrome(self, s: str, k: int) -> str:
        if len(s) == 1:
            if k == 1:
                return s
            else:
                return ""
                
        # Setup init counts and choose chars for k=1
        counts = [0 for i in range(26)]
        for c in s:
            counts[ord(c) - 97] += 1

        middleElement = ""
        for val in range(26):
            if counts[val] % 2:
                middleElement = chr(val + 97)
                counts[val] -= 1
            
            counts[val] //= 2

        finalArr = []
        self.solveRemaining(counts, k, finalArr)
        if finalArr:
            half = "".join(finalArr)
            return half + middleElement + half[::-1]
        else:
            return ""



