class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixCounts = {}
        for word in words:
            st = ""
            for char in word:
                st += char
                if not st in prefixCounts:
                    prefixCounts[st] = 1
                else:
                    prefixCounts[st] += 1
        
        results = []
        for word in words:
            total = 0
            st = ""
            for char in word:
                st += char
                if st in prefixCounts:
                    total += prefixCounts[st]
            
            results.append(total)

        return results
        