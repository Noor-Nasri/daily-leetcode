class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        possible = set(wordList)
        if not endWord in possible:
            return 0
    
        seen = set()
        seen.add(beginWord)
        cur = [beginWord]
        numChars = len(beginWord)
        steps = 1

        while cur:
            nextIter = []

            for word in cur:
                if word == endWord: return steps

                for i in range(numChars):
                    for c in range(26):
                        newWord = word[:i] + chr(97 + c) + word[i+1:]
                        if newWord in possible and not newWord in seen:
                            seen.add(newWord)
                            nextIter.append(newWord)
            
            steps += 1
            cur = nextIter
        return 0

        