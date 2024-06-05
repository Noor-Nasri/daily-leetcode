class Solution:
    cutoffs = None

    def convertToTitle(self, columnNumber: int) -> str:
        if not self.cutoffs:
            cutoffs = [0]
            total = 0
            for j in range(1, 7):
                total += pow(26, j)
                cutoffs.append(total)
            self.cutoffs = cutoffs
        
        letters = []
        for i in range(7, 0, -1):
            cutoff = self.cutoffs[i - 1]

            if columnNumber > cutoff:
                # Cant represent number with just future combinations
                nRepWithOneLess = pow(26, i - 1)
                shifted = columnNumber - cutoff - 1
                letter = shifted // nRepWithOneLess
                letters.append(letter)
                
                # Shift back one level for next iteration 
                columnNumber -= nRepWithOneLess * (letter + 1)

        
        return "".join(
            [chr(lett + 65) for lett in letters]
            )
        