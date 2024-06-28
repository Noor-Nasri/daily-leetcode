class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        numEdges = [0 for i in range(n)]
        for u, v in roads:
            numEdges[u] += 1
            numEdges[v] += 1
        
        numEdges = sorted(numEdges)
        total = 0
        for ind, occur in enumerate(numEdges):
            total += (ind + 1)*occur
        return total


        