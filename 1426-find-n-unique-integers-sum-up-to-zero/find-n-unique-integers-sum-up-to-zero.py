class Solution:
    def sumZero(self, n: int) -> List[int]:
        numbers = []
        if n % 2 == 1:
            numbers.append(0)
        
        for i in range(1, n // 2 + 1):
            numbers.append(i)
            numbers.append(-i)
        
        return numbers