# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        level = [root]
        totalSwaps = 0

        while level:
            # ensure it is sorted
            vals = [r.val for r in level]
            curIndices = {
                vals[ind] : ind for ind in range(len(vals))
            }
            correct = sorted(vals)
            for ind in range(len(vals)):
                val = vals[ind]
                expected = correct[ind]
                if val == expected:
                    continue
                
                curIndices[val] = curIndices[expected]
                vals[curIndices[expected]] = val
                vals[ind] = expected
                totalSwaps += 1

            # get next level
            nextLevel = []
            for r in level:
                if r.left != None:
                    nextLevel.append(r.left)
                if r.right != None:
                    nextLevel.append(r.right)
            
            level = nextLevel
        
        return totalSwaps