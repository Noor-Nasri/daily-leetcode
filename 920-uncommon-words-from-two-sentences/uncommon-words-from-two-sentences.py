class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        multiple = set()
        uncommon = set()

        for word in (s1 + " " + s2).split():
            if word in multiple: continue
            if word in uncommon:
                uncommon.remove(word)
                multiple.add(word)
            else:
                uncommon.add(word)
        
        return uncommon

        