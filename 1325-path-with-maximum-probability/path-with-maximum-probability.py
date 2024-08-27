from heapq import heapify, heappop, heappush

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        connections = [{} for j in range(n)]
        for ind in range(len(edges)):
            u, v = edges[ind]
            p = succProb[ind]

            connections[u][v] = p
            connections[v][u] = p

        seen = set()
        options = [(-1, start_node)]
        heapify(options)

        while options:
            negProp, node  = heappop(options)
            if node in seen: continue
            seen.add(node)
            
            if node == end_node: return -negProp
            
            for nextNode in connections[node]:
                if nextNode in seen: continue
                heappush(options, (negProp * connections[node][nextNode], nextNode))


        return 0


