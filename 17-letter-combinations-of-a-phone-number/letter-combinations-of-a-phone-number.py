class Solution:
    mappings = {
        '2' : list('abc'),
        '3' : list('def'),
        '4' : list('ghi'),
        '5' : list('jkl'),
        '6' : list('mno'),
        '7' : list('pqrs'),
        '8' : list('tuv'),
        '9' : list('wxyz'),
    }

    def letterCombinations(self, digits: str, ind = 0, string = "") -> List[str]:
        if not len(digits): return [] # edge case
        if ind == len(digits): return [string] # base case

        allCombos = []
        for possible in self.mappings[digits[ind]]:
            allCombos += self.letterCombinations(digits, ind + 1, string + possible)

        return allCombos
        