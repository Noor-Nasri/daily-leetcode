# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        cur = [root]
        ans = []

        while cur:
            ans.append([])

            nextNodes = []
            for node in cur:
                if node.left: nextNodes.append(node.left)
                if node.right: nextNodes.append(node.right)
                ans[-1].append(node.val)

            cur = nextNodes
        
        return ans


        