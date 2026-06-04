class Solution:
    # There might be some math trick here but we can just brute force it
    # O(n * num_digits) to loop through all vals between num1 and num2
    def waveCount(self, num):
        digits = [int(e) for e in str(num)]
        waves = 0

        for ind in range(1, len(digits) - 1):
            isPeak = digits[ind] > digits[ind-1] and digits[ind] > digits[ind+1]
            isValley = digits[ind] < digits[ind-1] and digits[ind] < digits[ind+1]
            if isPeak or isValley:
                waves += 1
        return waves

    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for num in range(num1, num2 + 1):
            total += self.waveCount(num)
        return total
        