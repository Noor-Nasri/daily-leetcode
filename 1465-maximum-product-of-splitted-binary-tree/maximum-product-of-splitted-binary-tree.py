# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def edgeSearch(self, node, sumAttachedToParent):
        if node == None:
            return 

        prod = self.nodeToSum[node] * sumAttachedToParent
        self.maxProd = max(self.maxProd, prod)
        self.edgeSearch(node.left, sumAttachedToParent + node.val + self.nodeToSum.get(node.right, 0))
        self.edgeSearch(node.right, sumAttachedToParent + node.val + self.nodeToSum.get(node.left, 0))
    
    def sumFill(self, node):
        if node == None:
            return 

        self.sumFill(node.left)
        self.sumFill(node.right)
        self.nodeToSum[node] = node.val + self.nodeToSum.get(node.left, 0) + self.nodeToSum.get(node.right, 0)


    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.nodeToSum = {}
        self.maxProd = 0
        self.sumFill(root)
        self.edgeSearch(root, 0)
        return self.maxProd % (10**9 + 7)
        