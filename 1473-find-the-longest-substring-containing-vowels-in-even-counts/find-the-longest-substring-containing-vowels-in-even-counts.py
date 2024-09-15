class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a" : 0, "e"  : 1, "i" : 2, "o" : 3, "u" : 4}
        seen = [0, 0, 0, 0, 0]
        all_seen = [seen[:]]

        for ind in range(len(s)):
            ch = s[ind]
            if ch in vowels:
                vowel_ind = vowels[ch]
                seen[vowel_ind] += 1
            all_seen.append(seen[::])

        best = 0
        for length in range(len(s), 0, -1):
            for ind_start in range(len(s) - length + 1):
                if all((all_seen[ind_start + length][i] - all_seen[ind_start][i]) % 2 == 0 for i in range(5)):
                    return length

        return 0



        