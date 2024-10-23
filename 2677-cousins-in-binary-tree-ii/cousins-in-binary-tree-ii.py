# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currentDepth = [root]
        sums = []
        siblingSums = {}

        while currentDepth:
            nextDepth = []
            total = 0

            for node in currentDepth:
                if node == None: continue
                total += node.val
                nextDepth.append(node.left)
                nextDepth.append(node.right)

                childSum = (node.left and node.left.val or 0) + (node.right and node.right.val or 0)
                siblingSums[node.left] = childSum
                siblingSums[node.right] = childSum

            sums.append(total)
            currentDepth = nextDepth
        
        sums = sums[::-1]
        currentDepth = [root]

        while currentDepth:
            nextDepth = []
            total = sums.pop()

            for node in currentDepth:
                if node == None: continue
                nextDepth.append(node.left)
                nextDepth.append(node.right)

                # look at the current total, subtract self and sibling
                if node in siblingSums:
                    newVal = total - siblingSums[node]
                else:
                    newVal = 0
                node.val = newVal
                    
            currentDepth = nextDepth

        return root
        
