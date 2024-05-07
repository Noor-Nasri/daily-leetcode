# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getBestSums(self, root: Optional[TreeNode]):
        if root == None:
            return (-100000, -100000)

        # Returns (best overall path, best attachable path)
        # Attachable means parent of root can be added to this path
        best_left, forced_left = self.getBestSums(root.left)
        best_right, forced_right = self.getBestSums(root.right)

        best_forced = max( # attachable paths are root, root+left, and root+right
            root.val, forced_left + root.val, forced_right + root.val) 

        best_overall = max(
            best_left, best_right, best_forced, 
            forced_left + forced_right + root.val)

        return (best_overall, best_forced)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.getBestSums(root)[0]
        