class Solution:
    def make_counter(self, words: List[str]):
        word_counts = {}
        for word in words:
            if not word in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1
        return word_counts

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        solutions = []
        word_len = len(words[0])
        if len(s) < word_len*len(words): return []

        for offset in range(word_len):
            # based on offset, we have a list of strings. Then use sliding window.
            string_words = []
            for ind in range(offset, len(s), word_len):
                if ind + word_len > len(s): break
                string_words.append(s[ind:ind+word_len])
            if len(string_words) < len(words): break
    
            # Track # of missing words per window
            word_counter = self.make_counter(words)
            for i in range(len(words)):
                include = string_words[i]
                if include in word_counter:
                    word_counter[include] -= 1

            # At most 30 words, so we wont bother too much with optimizing check
            if all(v == 0 for v in word_counter.values()):
                solutions.append(offset)
            
            for num_skip in range(1, len(string_words) - len(words) + 1):
                exclude = string_words[num_skip - 1]
                include = string_words[num_skip - 1 + len(words)]
                if exclude in word_counter:
                    word_counter[exclude] += 1
                
                if include in word_counter:
                    word_counter[include] -= 1

                if all(v == 0 for v in word_counter.values()):
                    solutions.append(offset + num_skip*word_len)
                

        return solutions
        