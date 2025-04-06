# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lowestCommonAnc(self, root):
        # returns (deepest possible node that contains the deepest leafs, depth of deepest leaf)
        if root.left == None and root.right == None:
            return root, 1
        
        if root.left == None or root.right == None:
            onlyChild = root.left or root.right
            bestRoot, depth = self.lowestCommonAnc(onlyChild)
            return bestRoot, depth + 1
        
        root1, depth1 = self.lowestCommonAnc(root.left)
        root2, depth2 = self.lowestCommonAnc(root.right)

        if depth1 == depth2:
            return root, depth1 + 1
        elif depth1 > depth2:
            return root1, depth1 + 1
        else:
            return root2, depth2 + 1

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        root, depth = self.lowestCommonAnc(root)
        return root