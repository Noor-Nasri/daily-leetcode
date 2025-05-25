class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # since its all even, it means:
        # When two strings match, they can be used on two sides of the palindrome
        # When the two characters within the string match, it can be used as a middle

        counts = {}
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        

        total_matched = 0
        middleFound = False
        for word in counts:
            if not counts[word]: 
                continue

            if word[0] == word[1]:
                # 6 or 7 occurs -> put 3 on each side -> 12 total chars
                total_matched += (counts[word] // 2) * 4

                # if it was 7, we can put the last one in the middle
                if counts[word] % 2 == 1:
                    middleFound = True
            else:
                altWord = word[1] + word[0]
                if altWord in counts:
                    total_matched += min(counts[word], counts[altWord])*4
                    counts[word] = 0
                    counts[altWord] = 0
            

        return total_matched + int(middleFound)*2