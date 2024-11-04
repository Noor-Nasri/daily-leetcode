class Solution:
    def compressedString(self, word: str) -> str:
        words = []
        charCount = [None, 0]

        for c in word:
            if c == charCount[0]:
                charCount[1] += 1
                if charCount[1] == 9:
                    words.append(f'{charCount[1]}{charCount[0]}')
                    charCount = [None, 0]
            else:
                if charCount[0] != None:
                    words.append(f'{charCount[1]}{charCount[0]}')

                charCount = [c, 1]
        
        if charCount[0] != None:
            words.append(f'{charCount[1]}{charCount[0]}')
        return "".join(words)

        