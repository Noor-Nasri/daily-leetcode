class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        numVowels = [0]
        cur = 0
        vowels = {"a", "e", "i", "o", "u"}

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                cur += 1
            
            numVowels.append(cur)
        
        ans = []
        for l, r in queries:
            ans.append(numVowels[r+1] - numVowels[l])
        
        return ans