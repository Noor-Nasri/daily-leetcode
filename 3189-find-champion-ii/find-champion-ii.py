class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        winners = set(i for i in range(n))
        for a, b in edges:
            winners.discard(b)
        
        if len(winners) == 1:
            return winners.pop()
        return -1
        