# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        cur = [root]
        averages = []

        while cur:
            total = 0
            nextIter = []

            for node in cur:
                if node.left != None: nextIter.append(node.left)
                if node.right != None: nextIter.append(node.right)

                total += node.val
            
            averages.append(total / len(cur))
            cur = nextIter

        return averages
        