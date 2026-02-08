# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def explore(self, root):
        if root == None:
            return 0
        
        depthL = self.explore(root.left)
        depthR = self.explore(root.right)
        if abs(depthL - depthR) > 1:
            self.balanced = False
        
        return max(depthL, depthR) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.explore(root)
        return self.balanced