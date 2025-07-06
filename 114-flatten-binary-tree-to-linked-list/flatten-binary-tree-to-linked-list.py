# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flattenRecursively(self, root):
        if root == None:
            return None, None

        # Returns head, tail
        if root.left != None and root.right != None:
            leftHead, leftTail = self.flattenRecursively(root.left)
            rightHead, rightTail = self.flattenRecursively(root.right)

            leftTail.right = rightHead 
            
            root.left = None
            root.right =  leftHead
            return root, rightTail
        
        elif root.left != None:
            leftHead, leftTail = self.flattenRecursively(root.left)
            root.left = None
            root.right =  leftHead
            return root, leftTail
        
        elif root.right != None:
            rightHead, rightTail = self.flattenRecursively(root.right)
            return root, rightTail
        
        else:
            return root, root


        

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenRecursively(root)
        