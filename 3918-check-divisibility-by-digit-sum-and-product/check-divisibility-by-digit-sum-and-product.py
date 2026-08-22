class Solution:
    def checkDivisibility(self, n: int) -> bool:
        values = [int(e) for e in str(n)]
        total, product = 0, 1
        for val in values:
            total += val
            product *= val
        
        return (n % (total + product)) == 0