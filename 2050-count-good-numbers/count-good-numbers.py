from math import ceil

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Per even index, we have 0, 2, 4, 6, 8 ==> 5 options
        # Per odd index, we have 2, 3, 5, 7 ==> 4 options
        numEven = ceil(n / 2)
        numOdd = n // 2

        answer = pow(5, numEven, 10**9 + 7) * pow(4, numOdd, 10**9 + 7)
        return answer % (10**9 + 7)
        