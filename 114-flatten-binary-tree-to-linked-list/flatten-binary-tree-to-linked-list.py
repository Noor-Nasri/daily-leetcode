# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flattenRecursively(self, root):
        # flatten and then return tail
        if root == None or (not root.left and not root.right):
            return root
        
        leftTail = self.flattenRecursively(root.left)
        rightTail = self.flattenRecursively(root.right)

        if leftTail:
            leftTail.right = root.right 
            root.right = root.left
            root.left = None

        return rightTail or leftTail
        


        

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenRecursively(root)
        