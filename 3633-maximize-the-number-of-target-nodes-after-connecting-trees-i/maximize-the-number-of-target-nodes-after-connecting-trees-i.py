class Solution:
    def buildBFSSolution(self, V, connections, starting_ind):
        cur = [starting_ind]
        seen = set(cur)
        found = 0
        for batch in range(V + 1):
            next_cur = []
            for u in cur:
                found += 1
                for v in connections[u]:
                    if v not in seen:
                        seen.add(v)
                        next_cur.append(v)
            cur = next_cur

        return found
            
                    
    def getConnList(self, edges, V):
        # Given x edges, we will return x-1 ints
        # val i <-> num of connections <= v away from node i
        connections = [[] for i in range(len(edges) + 1)]
        for u, v in edges:
            connections[u].append(v)
            connections[v].append(u)

        totals = []
        for starting_ind in range(len(edges) + 1):
            totals.append(self.buildBFSSolution(V, connections, starting_ind))
        
        return totals
        
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        lis1 = self.getConnList(edges1, k)
        lis2 = self.getConnList(edges2, k - 1)
        maxAddition = max(lis2)
        sol = [e + maxAddition for e in lis1]
        return sol

        