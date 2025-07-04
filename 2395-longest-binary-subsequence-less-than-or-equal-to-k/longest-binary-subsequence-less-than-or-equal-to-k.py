class Solution:
    # k = 5 <--> 101
    # Two cases: we make binary length = 3, or length < 3
    # For length < 3, it is super easy. Take last k-1 digits, then as many leading 0s as possible.
    # For length = 3, keep matching to earliest 1 or 0, as needed.
    #     If you need 1, you can instead take a 0 and all future ones will be less as well

    # Kind of annoying to do all that: Simpler answer is to just keep removing leading 1
    def longestSubsequence(self, s: str, k: int) -> int:
        while s and int(s, 2) > k:
            indOfOne = s.find('1')
            s = s[:indOfOne] + s[indOfOne + 1:]

        return len(s)