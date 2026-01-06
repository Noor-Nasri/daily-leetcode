# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        bestSum = root.val
        bestLevel = 1
        curNodes = [root]
        curLevel = 1

        while curNodes:
            newNodes = []
            curSum = 0
            for node in curNodes:
                curSum += node.val
                if node.left:
                    newNodes.append(node.left)
                if node.right:
                    newNodes.append(node.right)

            if curSum > bestSum:
                bestSum = curSum
                bestLevel = curLevel

            curLevel += 1
            curNodes = newNodes
        
        return bestLevel