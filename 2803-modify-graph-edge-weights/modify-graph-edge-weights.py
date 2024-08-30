from copy import deepcopy
from heapq import heapify, heappush, heappop 
 
class Solution:
    def getShortestPath(self, source, destination, target):
        visited = set()
        options = [(0, source, [])] # cost to reach, cur node, some modded edge on path
        heapify(options)

        while options:
            cost, node, modded = heappop(options)
            if node in visited: continue
            if node == destination:
                return [cost, modded]
            
            if cost > target: break
                    
            visited.add(node)

            for newNode in self.connections[node]:
                if newNode in visited: continue
                if (node, newNode) in self.adjustments:
                    continue # any path with this edge is >= target
                
                newCost = cost + self.connections[node][newNode]
                nextModded = modded

                if (node, newNode) in self.optionsToMod:
                    nextModded = modded[::]
                    nextModded.append((node, newNode))
                    nextModded.append((newNode, node))

                heappush(options, (newCost, newNode, nextModded))

        return [0, False]



    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        # My first solution for this was to generate ALL paths source -> dest, sort by distance and modify 1 edge per path.
        # It hit TLE at just n=18, because I need to store the whole path for each path when generating it.
        # But since n<=100, BFS is just O(100) so I can just get the shortest path every iteration, then modify 1 edge or end.
        # At most, we need to remove one edge every time we run BFS, until empty. Therefore O(n^3). 

        self.connections = [{} for i in range(n)]
        self.optionsToMod = set()
        for u, v, w in edges:
            if w == -1:
                w = 1
                self.optionsToMod.add((u, v))
                self.optionsToMod.add((v, u))
            self.connections[u][v] = w
            self.connections[v][u] = w

        foundOnePath = False
        self.adjustments = {} # (u, w) = new weight > 1

        while True:
            cost, modifiers = self.getShortestPath(source, destination, target)
            if not cost:
                break # No more paths
            if cost >= target:
                if cost == target:
                    foundOnePath = True
                break # No more self.adjustments needed


            if not modifiers:
                # Can't improve this path and its < target, its over
                return []
            
            u, v = modifiers[0]
            self.adjustments[(u, v)] = target - cost # Removes this edge from future checks
            self.adjustments[(v, u)] = target - cost
            foundOnePath = True

            # Speed up: all other edges can go to infinity
            includedEdges = set(modifiers)
            for op in self.optionsToMod:
                if not op in includedEdges:
                    self.adjustments[op] = target + 1
        
        if not foundOnePath:
            return []

        # Now, just need to print proper edges
        newEdges = []
        for u, v, w in edges:
            if w == -1: w = 1
            
            if (u, v) in self.adjustments:
                w += self.adjustments[(u, v)]

            newEdges.append([u, v, w])
        return newEdges
