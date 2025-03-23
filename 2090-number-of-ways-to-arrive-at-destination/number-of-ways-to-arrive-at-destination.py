from heapq import heapify, heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        maxNum = 10**9 + 7
        conns = [{} for i in range(n)]
        for u, v, t in roads:
            conns[u][v] = t
            conns[v][u] = t

        distArrays = [[-1, -1] for i in range(n)] # dist, numReach
        distArrays[0] = [0, 1] 
        seen = {0}

        options = [ (conns[0][e], e, 0) for e in conns[0] ]
        heapify(options) 

        while options:
            dist, node, prevNode = heappop(options)
            if node in seen: 
                if dist == distArrays[node][0]:
                    distArrays[node][1] += distArrays[prevNode][1]
                    distArrays[node][1] %= maxNum
                continue
            
            seen.add(node)
            distArrays[node][0] = dist
            distArrays[node][1] = distArrays[prevNode][1]
            for v in conns[node]:
                if v not in seen:
                    heappush(
                        options,
                        (dist + conns[node][v], v, node)
                    )
        
        return distArrays[n - 1][1]