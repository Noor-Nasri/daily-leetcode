from heapq import heappush, heappop

class Solution:
    # Okay so, what this word salad means is that we first choose disjoint parts within source,
    # Then each of those sections is able to flip any number of times using the original -> changed map
    # With this ability, what's the least cost to turn source into target

    # This seems like two questions: DP to segment the source and precompute cheapest routes
    # For each [original], we do djistras with connections based on [original] -> [changed]
    # So this would be 100 iterations * djistras(100 elements max). No problem

    # Then we can do DP based on ind = x
    # Option 0: If source[x] == target[x], go to ind + 1
    # Option 1->n: If source[x .. x + i] can be mapped to target[x .. x + 1], try that
    # Ignoring string checks, would be n^2 with n <= 1000 so that's also okay.
    # But we can't afford to build string as we expand pointer since thats n^3, so need to hash

    # Okay, so: Step 1 is convert all the original/changed into hash
    # Step 2: Build hash->hash map with minCost
    # Step 3: Do basic DP to solve

    def convertTableToHashes(self, strList):
        newList = []
        intermediateHashes = set()

        for string in strList:
            hashValue = 0
            for char in string:
                hashValue = (hashValue * 29 + ord(char) - 96) % self.MODVAL
                intermediateHashes.add(hashValue)
            newList.append(hashValue)
        
        return newList, intermediateHashes
    
    def buildCheapestCosts(self, root, connections):
        avail = [(0, root)]
        minCosts = {}
        while avail:
            curCost, node = heappop(avail)
            if node in minCosts and minCosts[node] < curCost:
                continue
            
            minCosts[node] = curCost
            for conn in connections.get(node, {}):
                newCost = curCost + connections[node][conn]
                if conn in minCosts and minCosts[conn] < newCost:
                    continue

                minCosts[conn] = newCost
                heappush(avail, (newCost, conn))
        
        return minCosts

    def dpSolve(self, sourceInd, sourceOrds, targetOrds, intermediateHashes):
        if sourceInd in self.sols:
            return self.sols[sourceInd]
        elif sourceInd == len(self.source):
            return 0

        options = []
        if self.source[sourceInd] == self.target[sourceInd]:
            remCost = self.dpSolve(sourceInd + 1,  sourceOrds, targetOrds, intermediateHashes)
            if remCost > -1:
                options.append(remCost)
        
        sourceHash = 0
        targetHash = 0
        for ind in range(sourceInd, len(self.source)):
            sourceHash = (sourceHash * 29 + sourceOrds[ind]) % self.MODVAL
            targetHash = (targetHash * 29 + targetOrds[ind]) % self.MODVAL
            if sourceHash in self.minCosts and targetHash in self.minCosts[sourceHash]:
                remCost = self.dpSolve(ind + 1, sourceOrds, targetOrds, intermediateHashes)
                if remCost > -1:
                    options.append(self.minCosts[sourceHash][targetHash] + remCost)
            
            if sourceHash not in intermediateHashes and sourceHash != targetHash:
                break

        if options:
            ans = min(options)
        else:
            ans = -1
        
        self.sols[sourceInd] = ans
        return ans

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        self.MODVAL = 10**9 + 7
        self.source = source
        self.target = target

        hashedOriginals, intermediateHashes = self.convertTableToHashes(original)
        hashedChanged, _ = self.convertTableToHashes(changed)
        connections = {}
        for ind in range(len(hashedOriginals)):
            s, t = hashedOriginals[ind], hashedChanged[ind]
            if s not in connections:
                connections[s] = {}

            if t in connections[s]:
                connections[s][t] = min(connections[s][t], cost[ind])
            else:
                connections[s][t] = cost[ind]

        self.minCosts = {}
        for s in connections:
            self.minCosts[s] = self.buildCheapestCosts(s, connections)

        self.sols = {}
        sourceOrds = [ord(source[ind]) - 96 for ind in range(len(source))]
        targetOrds = [ord(target[ind]) - 96 for ind in range(len(target))]
        ans = self.dpSolve(0, sourceOrds, targetOrds, intermediateHashes)

        return ans
