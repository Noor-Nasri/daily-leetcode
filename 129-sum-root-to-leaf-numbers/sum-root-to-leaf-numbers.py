# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumPaths(self, root, total):
        total = total*10 + root.val

        if ((root.left == None) and (root.right == None)):
            return total
        
        children_totals = 0
        if (root.left != None):
            children_totals += self.sumPaths(root.left, total)

        if (root.right != None):
            children_totals += self.sumPaths(root.right, total)

        return children_totals

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sumPaths(root, 0)
        