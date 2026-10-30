class Solution:
    # We can just do djisktras, except instead of visiting a node once we can visit it if we get a smaller curRepeatCount
    # Since k <= 50, this just means we visit each node at most 50 times, so we should be fine.

    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        connections = [{} for i in range(n)]
        for u, v, w in edges:
            curVal = connections[u].get(v, 100000)
            connections[u][v] = min(w, curVal)
        
        pq = [(0, 1, 0)] # curCost, curRepeatCount, curNode
        explored = {} # we can re-explore new nodes (always higher cost cuz pq), as long as smaller repCount

        while pq:
            curCost, curRepeatCount, curNode = heappop(pq)
            if curNode == n - 1:
                return curCost

            elif curNode in explored and explored[curNode] <= curRepeatCount:
                continue
            
            explored[curNode] = curRepeatCount
            for conn in connections[curNode]:
                cost = curCost + connections[curNode][conn]
                repCount = curRepeatCount + 1 if labels[conn] == labels[curNode] else 1

                if repCount > k or (conn in explored and explored[conn] <= cost):
                    continue
                
                newElement = (cost, repCount, conn)
                heappush(pq, newElement)

        return -1
        