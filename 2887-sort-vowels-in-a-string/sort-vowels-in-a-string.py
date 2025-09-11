class Solution:
    def sortVowels(self, s: str) -> str:
        vowelChars = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        allChars = []
        vowels = []

        for c in s:
            if c in vowelChars:
                allChars.append('.')
                vowels.append(c)
            else:
                allChars.append(c)

        vowels = sorted(vowels, reverse = True)
        for ind in range(len(allChars)):
            if allChars[ind] == ".":
                allChars[ind] = vowels.pop()
        
        return "".join(allChars)