# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solveDiameter(self, root):
        # return max distance within tree, max distance between any node and self
        if root == None: return 0, 0 
        
        maxDistLeft, DistFromLeft = self.solveDiameter(root.left)
        maxDistRight, DistFromRight = self.solveDiameter(root.right)

        chainedDist = DistFromLeft + DistFromRight + 1
        maxDist = max(maxDistLeft, maxDistRight, chainedDist)
        maxDistToRoot = max(DistFromLeft, DistFromRight) + 1

        return maxDist, maxDistToRoot

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDist, _ = self.solveDiameter(root)
        return maxDist - 1