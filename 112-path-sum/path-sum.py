# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            return targetSum == root.val
        
        remainingSum = targetSum - root.val
        return (self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum))