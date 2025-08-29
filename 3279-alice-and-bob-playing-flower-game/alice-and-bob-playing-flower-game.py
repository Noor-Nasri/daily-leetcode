class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # So simply put, x + y must be odd for alice to win.
        # So, how many pairs of (x,y) exist for 1 <= x <= n, 1 <= y <= m?
        # Even + Even = Even, and Odd + Odd = Even, but Even + Odd is odd

        numEvenX = n // 2
        numEvenY = m // 2
        numOddX = (n + 1) // 2
        numOddY = (m + 1) // 2

        return numEvenX * numOddY + numOddX * numEvenY
