class Solution:
    # Seems easier to just check all valid 3 dig numbers
    # We just want to make sure all digits are available 

    def validDigits(self, available, required):
        for i in range(10):
            if required[i] > available[i]:
                return False
        return True

    def totalNumbers(self, digits: List[int]) -> int:
        available = [0 for i in range(10)]
        for d in digits:
            available[d] += 1

        found = 0
        for num in range(100, 1000, 2):
            required = [0 for i in range(10)]
            required[num // 100] += 1
            required[(num % 100) // 10] += 1
            required[(num % 100) % 10] += 1

            if self.validDigits(available, required):
                found += 1
                        
        return found
            
        