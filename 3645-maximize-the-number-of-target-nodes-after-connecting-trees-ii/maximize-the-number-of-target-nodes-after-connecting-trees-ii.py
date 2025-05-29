class Solution:
    def buildBFSSolution(self, connections, starting_ind):
        cur = [starting_ind]
        seen = set(cur)
        found = [0, 0]
        batch = 0
        while cur:
            next_cur = []
            for u in cur:
                found[batch % 2] += 1
                for v in connections[u]:
                    if v not in seen:
                        seen.add(v)
                        next_cur.append(v)
                
            cur = next_cur
            batch += 1

        return found
            
    def buildTotals(self, root, parent, evenOdd, solution):
        self.totals[root] = solution[evenOdd]
        evenOdd = 1 - evenOdd

        for conn in self.connections[root]:
            if conn == parent: continue
            self.buildTotals(conn, root, evenOdd, solution)
        
        
    def getConnList(self, edges, evenOdd):
        # Given x edges, we will return x-1 ints
        # val i <-> num of connections <= v away from node i
        self.connections = [[] for i in range(len(edges) + 1)]
        for u, v in edges:
            self.connections[u].append(v)
            self.connections[v].append(u)

        self.totals = [0 for i in range(len(edges) + 1)]
        for r in range(len(edges) + 1):
            if len(self.connections[r]) == 1:
                root = r
                break
        
        numEven, numOdd = self.buildBFSSolution(self.connections, root)
        self.buildTotals(root, None, evenOdd, [numEven, numOdd])
        
        return self.totals
        
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        lis1 = self.getConnList(edges1, 0)
        lis2 = self.getConnList(edges2, 1)
        maxAddition = max(lis2)
        sol = [e + maxAddition for e in lis1]
        return sol

        