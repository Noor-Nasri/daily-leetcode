class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        possible = set(wordList)
        if not endWord in possible:
            return 0
    
        chars = [chr(c) for c in range(97, 97+26)]
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
                    for c in chars:
                        newWord = word[:i] + c + word[i+1:]
                        if not newWord in seen and newWord in possible:
                            seen.add(newWord)
                            nextIter.append(newWord)
            
            steps += 1
            cur = nextIter
        return 0

        