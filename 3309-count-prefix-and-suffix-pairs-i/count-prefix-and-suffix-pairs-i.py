class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        tot = 0
        for ind1 in range(len(words)):
            for ind2 in range(ind1 + 1, len(words)):
                prefix = words[ind1]
                if prefix == words[ind2][:len(prefix)] == words[ind2][-len(prefix):]:
                    tot += 1
        
        return tot