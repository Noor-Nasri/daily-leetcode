class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for number in range(n, 1000):
            digits = [int(e) for e in str(number)]
            prod = math.prod(digits)
            if prod % t == 0:
                return number
                