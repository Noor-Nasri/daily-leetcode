class Solution:
    # Okay, so for each query, all we actually care about is distance.
    # Then for any d=dist, would need some form of DP to make all these queries efficient
    # For d=5 (ie 5 edges), we would have 5, 3, or 1 edges at 1. So 5C5 + 5C3 + 5C1
    # For d=7, we would have 7, 5, 3, or 1. 7C7 + 7C5 + 7C3 + 7C1. 
    # How do we connect this? The denominators are totally different, so we cant just add S(d-2)

    # Can we forget the math and just do literal DP? At each node we have two options.
    # DP(remDist, isEven) -> set next edge to 1 (flip isEven) or 2 (keep isEven).
    # Then this becomes super simple addition and modulo! Why didn't I do this last time lol

    # I got TLE, but its actually because the trivial part of calculating dist needs to be optimized
    # I thought it was O(logn) to trace ancestor but this isnt guaranteed to be a balanced tree.
    # Balancing the tree or doing BS on all ancestors are both complicated .. 
    # Maybe we do something cheeky like storing the ancestors of d=1, 2, 4, 8, 16, etc.
    # This allows us to cut down the dist in O(logN) but its also a bit annoying ..

    # I'm ngl this took me like the entire morning to get properly :(

    def makeChildMapping(self, edges):
        # Transform edges to (root, [u] -> [list of children])
        viableRoots = {i for i in range(1, len(edges) + 2)}
        children = [[] for i in range(len(edges) + 2)]
        for u, v in edges:
            if v in viableRoots:
                viableRoots.remove(v)
            
            children[u].append(v)
        
        return viableRoots.pop(), children

    # We now want to turn child mapping into [v] -> [parent at d=1, d=2, d=4, d=8, ...] 
    # So we do DFS to track full parent chain, ie O(n) memory, then store log(n) per node
    def makeAncestryChains(self, fullAncestorChain, curInd):
        fullAncestorChain.append(curInd)
        compactAncestorChain = []
        ancestorDist = 1
        while ancestorDist < len(fullAncestorChain):
            compactAncestorChain.append(fullAncestorChain[-ancestorDist - 1])
            ancestorDist *= 2

        if curInd != self.root and compactAncestorChain[-1] != self.root:
            compactAncestorChain.append(self.root) # Add root to chain so we can always connect nodes

        self.ancestorChainMap[curInd] = compactAncestorChain
        self.depthMap[curInd] = len(fullAncestorChain) - 1

        for childInd in self.childrenMap[curInd]:
            self.makeAncestryChains(fullAncestorChain, childInd)

        fullAncestorChain.pop()
    
    
    def getBalancedNodes(self, node1, node2):
        # Take u, v and return one of them as its ancestor, matching depth of the higher one
        depth1, depth2 = self.depthMap[node1], self.depthMap[node2]
        if depth1 == depth2:
            return node1, node2, 0
        elif depth1 < depth2:
            parent, child = node1, node2
        else:
            parent, child = node2, node1

        # Start from child, and trace chain all the way until we have depth of parent
        originalDepth, desiredDepth = self.depthMap[child], self.depthMap[parent]
        curChild = child
        while self.depthMap[curChild] != desiredDepth:
            for ancestorOfChild in self.ancestorChainMap[curChild]:
                if self.depthMap[ancestorOfChild] < desiredDepth:
                    break
                curChild = ancestorOfChild

        return parent, curChild, originalDepth - desiredDepth

    # Given the 2 nodes on the same level, just traverse up their trees in unison to get ECA in log(n)^2
    def getEarliestCommonAncestorFromBalancedNodes(self, node1, node2):
        if node1 == node2:
            return node1

        tempAncestor1, tempAncestor2 = node1, node2
        while True:
            chain1, chain2 = self.ancestorChainMap[tempAncestor1], self.ancestorChainMap[tempAncestor2]
            if chain1[0] == chain2[0]:
                return chain1[0]
            
            for uncommonAncestorInd in range(len(chain1)):
                if chain1[uncommonAncestorInd] == chain2[uncommonAncestorInd]:
                    # We found a common ancestor, lets hone in on last known uncommons to find true earliest
                    break
                
                tempAncestor1, tempAncestor2 = chain1[uncommonAncestorInd], chain2[uncommonAncestorInd]

        
    def solveCombinatoric(self, remDist, isOdd):
        uid = (remDist, isOdd)
        if remDist == 0:
            return isOdd
        elif uid in self.sols:
            return self.sols[uid]
        
        MOD = 10**9 + 7
        op1 = self.solveCombinatoric(remDist - 1, isOdd) % MOD
        op2 = self.solveCombinatoric(remDist - 1, 1 - isOdd) % MOD
        self.sols[uid] = (op1 + op2) % MOD
        return self.sols[uid]


    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        self.root, self.childrenMap = self.makeChildMapping(edges)
        self.ancestorChainMap = {}
        self.depthMap = {}
        self.makeAncestryChains([], self.root)

        #print(self.ancestorChainMap)
        #print(self.depthMap)

        answers = []
        self.sols = {}
        for u, v in queries:
            #print("===== Solving for", u, v, "=====")
            elevatedU, elevatedV, initDist = self.getBalancedNodes(u, v)
            #print("We elevate this to", elevatedU, elevatedV, "for a cost of", initDist)
            earliestAncestor = self.getEarliestCommonAncestorFromBalancedNodes(elevatedU, elevatedV)
            #print("The earliest common ancestor is", earliestAncestor)
            dist = initDist + 2*(self.depthMap[elevatedU] - self.depthMap[earliestAncestor])
            combs = self.solveCombinatoric(dist, 0)
            #print("Final distance is", dist, "which has", combs, "combinations")
            answers.append(combs)
        
        return answers
