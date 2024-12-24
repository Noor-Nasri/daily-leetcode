class TreeNode:
    def __init__(self):
        self.children = []
    
    def setDepth(self, parent):
        # depth of subtree rooted at self
        self.depth = 1
        for node in self.children:
            if node == parent: continue
            node.setDepth(self)
            self.depth = max(self.depth, 1 + node.depth)

    def getMaxDiameter(self, parent):
        maxDiameter = 0
        maxDepths = [0, 0]
        for node in self.children:
            if node == parent: continue
            maxDiameter = max(maxDiameter, node.getMaxDiameter(self))

            if node.depth > maxDepths[0]:
                maxDepths[1] = maxDepths[0]
                maxDepths[0] = node.depth
            elif node.depth > maxDepths[1]:
                maxDepths[1] = node.depth


        maxDiameter = max(maxDiameter, 1 + maxDepths[0] + maxDepths[1])
        return maxDiameter


class Solution:
    def getRootFromEdges(self, edges):
        nodes = [TreeNode() for i in range(len(edges) + 1)]
        for u, v in edges:
            nodes[u].children.append(nodes[v])
            nodes[v].children.append(nodes[u])
        
        # expecting clean input
        for node in nodes:
            if len(node.children) <= 1:
                node.setDepth(None)
                return node

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        root1 = self.getRootFromEdges(edges1)
        root2 = self.getRootFromEdges(edges2)

        diameter1 = root1.getMaxDiameter(None)
        diameter2 = root2.getMaxDiameter(None)
        return max(diameter1 - 1, diameter2 - 1, diameter1 // 2 + diameter2 // 2 + 1)
