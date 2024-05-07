class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        valueMappings = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        lastValue = valueMappings[s[0]]

        for i in range(1, len(s)):
            val = valueMappings[s[i]]

            if val <= lastValue:
                total += lastValue
            else:
                total -= lastValue
            
            lastValue = val
        
        return total + lastValue
        