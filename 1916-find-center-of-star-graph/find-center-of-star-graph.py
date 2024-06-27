class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counts = {}
        numNodes = 0
        for u, v in edges:
            if not u in counts:
                counts[u] = 0
                numNodes += 1

            if not v in counts:
                counts[v] = 0
                numNodes += 1
            
            counts[u] += 1
            counts[v] += 1

        
        for node in counts:
            if counts[node] == numNodes - 1:
                return node
        
        return -1
        