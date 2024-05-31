# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        nodes = [root]
        while nodes:
            nextIter = []
            for i in range(len(nodes)):
                first = nodes[i]
                second = nodes[len(nodes) - 1 - i]
                
                # Symmetrically have no children
                if first == None and second == None: continue
                if first == None or second == None: return False
                if first.val != second.val: return False
                
                # append next round
                if first:
                    nextIter.append(first.left)
                    nextIter.append(first.right)

            nodes = nextIter


        return True # shouldnt reach
        