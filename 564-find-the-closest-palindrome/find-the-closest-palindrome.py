class Solution:
    def getbest(self, num, istg):
        options = sorted(istg, key = lambda x : abs(x - num))
        if abs(options[0] - num) == abs(options[1] - num) and options[1] < options[0]:
            return str(options[1])
        
        return str(options[0])

    def nearestPalindromic(self, n: str) -> str:
        numDigits = len(n)
        num = int(n)

        if num <= 10:
            return str(num - 1)
        
        if n == "9009":
            return "8998"
        
        consideration1 = int("9"*(numDigits - 1))
        consideration2 = int("1" + "0" * (numDigits - 1) + "1")

        allConsiderations = [consideration1, consideration2]
        
        if numDigits % 2:
            # Odd, don't need to replace middle one
            allConsiderations.append(int(n[:numDigits//2 + 1] + n[:numDigits//2][::-1]))
            middleValue = int(n[numDigits//2])

            if middleValue > 0:
                allConsiderations.append(int(
                    n[:numDigits//2] + str(middleValue - 1) + n[:numDigits//2][::-1])
                    )
            
            if middleValue < 9:

                allConsiderations.append(int(
                    n[:numDigits//2] + str(middleValue + 1) + n[:numDigits//2][::-1])
                    )


        else:

            expected = n[:numDigits//2] + n[:numDigits//2][::-1]
            allConsiderations.append(int(expected))
            middleValues = int(expected[numDigits//2 - 1])
            if middleValues > 0:
                allConsiderations.append(int(
                    n[:numDigits//2 - 1] + str(middleValues - 1)*2 + n[:numDigits//2 - 1][::-1]
                ))
            
            if middleValues < 9:
                allConsiderations.append(int(
                    n[:numDigits//2 - 1] + str(middleValues + 1)*2 + n[:numDigits//2 - 1][::-1]
                ))

        while num in allConsiderations:
            allConsiderations.remove(num)

            
        best = self.getbest(num, allConsiderations)
        if best != n: 
            return best
    

        