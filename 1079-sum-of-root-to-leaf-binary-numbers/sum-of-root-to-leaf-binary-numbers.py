# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, sumToNode):
        curSum = sumToNode * 2 + root.val
        if root.left == None and root.right == None:
            return curSum
        else:
            paths = []
            if root.left:
                paths.append(self.traverse(root.left, curSum))
            if root.right:
                paths.append(self.traverse(root.right, curSum))
            
            return sum(paths)


    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)
