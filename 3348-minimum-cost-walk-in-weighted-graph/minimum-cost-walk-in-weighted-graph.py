class Solution:
    def explore(self, node, island):
        self.islands[node] = island

        for conn in self.connections[node]:
            self.islandCost &= self.connections[node][conn]

            if self.islands[conn] == -1:
                self.explore(conn, island)

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # everything in the same island will have same distances, because the min dist is AND of every edge possible
        self.connections = [{} for i in range(n)]
        for u, v, w in edges:
            if u in self.connections[v]:
                self.connections[v][u] &= w
                self.connections[u][v] &= w
            else:
                self.connections[v][u] = w
                self.connections[u][v] = w

        self.islands = [-1 for i in range(n)]
        islandCosts = {}
        islandCount = 0
        for node in range(n):
            if self.islands[node] == -1:
                self.islandCost = 131071 # 11..1
                self.explore(node, islandCount)
                islandCosts[islandCount] = self.islandCost
                islandCount += 1

        results = []
        for u, v in query:
            if self.islands[u] == self.islands[v]:
                results.append(islandCosts[self.islands[u]])
            else:
                results.append(-1)
        
        return results