# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSmallestTreeWithDeepLeaves(self, root):
        # Returns (bestTreeNode, depth from root)
        if not root:
            return (None, 0)

        bestL, depthL = self.getSmallestTreeWithDeepLeaves(root.left)
        bestR, depthR = self.getSmallestTreeWithDeepLeaves(root.right)

        if depthL == depthR:
            return (root, depthL + 1)
        elif depthL > depthR:
            return (bestL, depthL + 1)
        else:
            return (bestR, depthR + 1)

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node, fullDepth = self.getSmallestTreeWithDeepLeaves(root)
        return node