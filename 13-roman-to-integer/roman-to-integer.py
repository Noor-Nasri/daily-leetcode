class Solution:
    def romanToInt(self, s: str) -> int:
        valueMappings = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        lastValue = 0 #valueMappings[s[0]]
        total = 0

        for c in s:
            val = valueMappings[c]
            
            if val <= lastValue:
                total += lastValue
            else:
                total -= lastValue
            
            lastValue = val
        
        return total + lastValue
        