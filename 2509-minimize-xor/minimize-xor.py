class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # we want to match 1s with 1s to flip them to 0s. 

        numOnes = sum([int(e) for e in str(bin(num2)[2:])])
        bin1 = str(bin(num1))[2:]
        if numOnes >= len(bin1):
            result = ["1" for i in range(numOnes)]
        else:
            result = ["0" for i in range(len(bin1))]
            searchMode = "1"
            ind = 0

            while numOnes:
                if bin1[ind] == searchMode:
                    result[ind] = "1"
                    numOnes -= 1
                
                ind += searchMode == "1" and 1 or -1
                if ind == len(bin1):
                    ind = len(bin1) - 1
                    searchMode = "0"

        

        return int("".join(result), 2)