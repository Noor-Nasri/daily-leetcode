class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        letterCounts = [0 for i in range(26)]
        for c in s:
            letterCounts[ord(c) - 97] += 1
        
        bestStr = []
        remaining_inds = [e for e in range(26)]
        for letter_ind in range(25, -1, -1):
            letter = chr(letter_ind + 97)

            if remaining_inds and remaining_inds[-1] == letter_ind:
                remaining_inds.pop()
            if not letterCounts[letter_ind]: 
                continue
                

            while letterCounts[letter_ind]:
                useCount = min(repeatLimit, letterCounts[letter_ind])
                for it in range(useCount): bestStr.append(letter)
                letterCounts[letter_ind] -= useCount

                if letterCounts[letter_ind]: # need a filler one
                    while remaining_inds and not letterCounts[remaining_inds[-1]]:
                        remaining_inds.pop()
                    if not remaining_inds:
                        break
                    
                    letterCounts[remaining_inds[-1]] -= 1
                    bestStr.append(chr(remaining_inds[-1] + 97))
                
        return "".join(bestStr)