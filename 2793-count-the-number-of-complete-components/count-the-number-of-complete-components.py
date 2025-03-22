class Solution:
    def explore(self, node, expectedNodes):
        valid = len(self.connections[node]) == len(expectedNodes) - 1

        for conn in self.connections[node]:
            if conn not in expectedNodes:
                valid = False
            
            if conn not in self.visited:
                self.visited.add(conn)
                if not self.explore(conn, expectedNodes):
                    valid = False

        return valid

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = set()
        self.connections = [[] for i in range(n)]
        
        for u, v in edges:
            self.connections[u].append(v)
            self.connections[v].append(u)
        
        total = 0
        for node in range(n):
            if node not in self.visited:
                self.visited.add(node)
                expectedNodes = set(self.connections[node])
                expectedNodes.add(node)

                if self.explore(node, expectedNodes):
                    total += 1
        
        return total
