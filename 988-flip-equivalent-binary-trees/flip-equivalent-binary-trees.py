# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getChildren(self, root):
        if root.left == None and root.right == None: return []
        elif root.left == None: return [root.right]
        elif root.right == None: return [root.left]
        elif root.right.val < root.left.val: return [root.right, root.left]
        return [root.left, root.right]

    def checkChildren(self, root1, root2):
        # swaps children if needed, then make sure they match and keep going
        children1 = self.getChildren(root1)
        children2 = self.getChildren(root2)
        if len(children1) != len(children2):
            return False
        
        for i in range(len(children1)):
            if not self.checkEquiv(children1[i], children2[i]):
                return False
        
        return True

    def checkEquiv(self, root1, root2):
        if (root1.val != root2.val): return False
        return self.checkChildren(root1, root2)


    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (root1 == None or root2 == None): return root1==root2
        return self.checkEquiv(root1, root2)
        