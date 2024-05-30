# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxDepth(self, root):
        if (root == None): return 0
        return 1 + max(self.getMaxDepth(root.left), self.getMaxDepth(root.right))
        

    def zigzagHelper(self, root, depth, solution):
        if (root == None): return
        solution[depth].append(root.val)
        self.zigzagHelper(root.left, depth + 1, solution)
        self.zigzagHelper(root.right, depth + 1, solution)



    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        solution = [[] for i in range(self.getMaxDepth(root))]
        self.zigzagHelper(root, 0, solution)

        for i in range (1, len(solution), 2):
            solution[i] = solution[i][::-1]

        return solution
        