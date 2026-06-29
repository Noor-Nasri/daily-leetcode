class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # idrc about optimizing this with trie or pre-hash. Just n^2 and done
        count = 0
        for s in patterns:
            if s in word:
                count += 1
        
        return count
