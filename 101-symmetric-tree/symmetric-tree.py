# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        nodes = [root]
        while True:
            # Check still equal
            allNull = True
            for i in range(len(nodes)//2+1):
                first = nodes[i]
                second = nodes[len(nodes) - 1 - i]
                
                # Symmetrically have no children
                if first == None and second == None: continue
                
                allNull = False
                if first == None or second == None: return False
                if first.val != second.val: return False

            if allNull: return True

            # Next round BFS
            nextIter = []
            for node in nodes:
                if node == None:
                    nextIter.append(None)
                    nextIter.append(None)
                else:
                    nextIter.append(node.left)
                    nextIter.append(node.right)
            
            nodes = nextIter


        return True # shouldnt reach
        