class TreeNode:
    def __init__(self, ind, val):
        self.ind = ind
        self.val = val
        self.children = []
    
    def offsetCostByBob(self, parent, curDepth, bobInd):
        # adjusts value if bob will reach our gate first or at the same time
        bobDepthConfirmed = None
        
        if self.ind == bobInd:
            bobDepthConfirmed = 0
        else:
            for node in self.children:
                if node == parent:
                    continue
                
                bobDepth = node.offsetCostByBob(self, curDepth + 1, bobInd)
                if bobDepth != None:
                    bobDepthConfirmed = bobDepth + 1
                    break
        
        if bobDepthConfirmed != None:
            if bobDepthConfirmed == curDepth:
                self.val //= 2
            elif bobDepthConfirmed < curDepth:
                self.val = 0

        return bobDepthConfirmed

    def maxProfit(self, parent):
        bestPath = None
        for node in self.children:
            if node == parent:
                continue
            
            option = node.maxProfit(self)
            if bestPath == None or option > bestPath:
                bestPath = option
        
        if bestPath == None:
            bestPath = 0
        
        bestPath += self.val
        return bestPath

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # O(n) solution: we build the tree then adjust the rewards based on bob, then just solve all path rewards

        nodes = [TreeNode(ind, amount[ind]) for ind in range(len(amount))]
        for u, v in edges:
            nodes[u].children.append(nodes[v])
            nodes[v].children.append(nodes[u])
        
        root = nodes[0]
        root.offsetCostByBob(None, 0, bob)

        return root.maxProfit(None)