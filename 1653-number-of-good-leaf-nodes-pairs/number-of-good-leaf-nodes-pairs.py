# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solvePairs(self, root, distance):
        if root == None: return []
        if root.left == None and root.right == None: 
            return [1] # Parent needs 1 step to reach here
        
        pairs_left = self.solvePairs(root.left, distance)
        pairs_right = self.solvePairs(root.right, distance)

        # Now check if the pairs work
        for dist1 in pairs_left:
            for dist2 in pairs_right:
                if (dist1 + dist2) <= distance:
                    self.total += 1 # Found a pair
        
        root_dists = pairs_left + pairs_right
        for i in range(len(root_dists)):
            root_dists[i] += 1
        
        return root_dists


    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.total = 0
        self.solvePairs(root, distance)
        return self.total
        