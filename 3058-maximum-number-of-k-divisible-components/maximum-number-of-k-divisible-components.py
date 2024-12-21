class TreeNode:
    def __init__(self, val):
        self.connections = []
        self.val = val


    def solveSplits(self, parent, k):
        # Returns (num splits, remaining total)
        # Splits the moment we can, to maximize splits
        totalSplits = 0
        totalValue = self.val

        for node in self.connections:
            if node == parent: continue
            extraSplits, remTotal = node.solveSplits(self, k)
            totalSplits += extraSplits
            totalValue += remTotal

        if totalValue % k == 0:
            return [totalSplits + 1, 0]
        
        return [totalSplits, totalValue]


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n == 1: return 1
        
        nodes = [TreeNode(values[i]) for i in range(n)]

        for u, v in edges:
            nodes[u].connections.append(nodes[v])
            nodes[v].connections.append(nodes[u])
        
        for possibleRoot in nodes:
            if len(possibleRoot.connections) == 1:
                rootNode = possibleRoot
                break
        
        numSplit, remaining = rootNode.solveSplits(None, k)
        assert(remaining == 0)
        return numSplit
        