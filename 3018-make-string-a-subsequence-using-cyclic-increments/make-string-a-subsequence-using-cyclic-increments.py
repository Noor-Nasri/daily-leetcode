class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Each char in str1 can be two options (+0, +1)
        # Greedy idea: include elements in the subsequence as soon as they work
        # This works because you can always exclude the next, other correct, choice

        ind1 = 0
        ind2 = 0

        while ind1 < len(str1) and ind2 < len(str2):
            optional_char = ord(str1[ind1]) + 1
            if optional_char > ord('z'):
                optional_char = ord('a')
            optional_char = chr(optional_char)

            if str2[ind2] == str1[ind1] or str2[ind2] == optional_char:
                # This char in str2 can be made with this char in str1
                ind1 += 1
                ind2 += 1
            else:
                ind1 += 1
        
        return ind2 == len(str2)