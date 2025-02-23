# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeNode(self, value, depth, treeStack):
        newNode = TreeNode(value)
        if depth == 0: 
            return newNode

        while len(treeStack) != depth:
            treeStack.pop()
        
        parentNode = treeStack[-1]
        if parentNode.left == None:
            parentNode.left = newNode
        else:
            parentNode.right = newNode
        
        return newNode

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        treeStack = []
        curDepth = 0
        curVal = []

        for c in traversal:
            if c == "-":
                if curVal:
                    treeStack.append(self.makeNode(int("".join(curVal)), curDepth, treeStack))
                    curDepth = 1
                    curVal = []
                else:
                    curDepth += 1
            else:
                curVal.append(c)
        

        treeStack.append(self.makeNode(int("".join(curVal)), curDepth, treeStack))
        return treeStack[0]
    