class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_indices = {}
        left = 0
        maxLen = 0

        for right in range(len(s)):
            char = s[right]
            if char in seen_indices:
                for ind_prev in range(left, seen_indices[char]):
                    del seen_indices[s[ind_prev]]
                left = seen_indices[char] + 1
            
            seen_indices[char] = right
            maxLen = max(maxLen, right - left + 1)

        return maxLen
        