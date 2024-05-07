# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getRelevantData(self, root):
        # Returns (best diff, min, max)

        smallest_diff = 1000000
        minimal = root.val
        maximal = root.val

        if (root.left != None):
            smallest_diff_left, min_left, max_left = self.getRelevantData(root.left)

            smallest_diff = min(
                smallest_diff, smallest_diff_left, root.val - max_left
                )
            minimal = min_left
        
        if (root.right != None):
            smallest_diff_right, min_right, max_right = self.getRelevantData(root.right)

            smallest_diff = min(
                smallest_diff, smallest_diff_right,  min_right - root.val
                )
            maximal = max_right
        
        return (smallest_diff, minimal, maximal)


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return self.getRelevantData(root)[0]