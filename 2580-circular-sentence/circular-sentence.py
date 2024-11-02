class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if len(sentence) != len(sentence.strip()): return False
        if "  " in sentence: return False
        words = sentence.split()
        for i in range(len(words)):
            if words[i][-1] != words[(i + 1) % len(words)][0]:
                return False
        
        return True

        