class Solution:
    # Isn't this just the biggest digit??
    # Like if we have 789, then we do 111 + 111 + 111 until 777. Then add 11 + 1.
    # With 9 numbers we just choose 1s in the places where we still need more.
    def minPartitions(self, n: str) -> int:
        return max([int(e) for e in str(n)])
        