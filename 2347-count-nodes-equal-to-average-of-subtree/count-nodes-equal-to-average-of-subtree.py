# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Pretty simple, just one pass through the tree
# Each node returns (total sum, num nodes) and verifies if its equal to the avg based on children. 
class Solution:
    def solve(self, root):
        if root == None:
            return (0, 0)
        
        sumLeft, countLeft = self.solve(root.left)
        sumRight, countRight = self.solve(root.right)
        sumAll = sumLeft + sumRight + root.val
        countAll = countLeft + countRight + 1

        if sumAll // countAll == root.val:
            self.found += 1
        
        return (sumAll, countAll)

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.found = 0
        self.solve(root)
        return self.found