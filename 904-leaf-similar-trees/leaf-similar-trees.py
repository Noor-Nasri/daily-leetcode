# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterateTillLeaf(self, tree):
        while tree[-1].left or tree[-1].right:
            nextElement = tree.pop()
            if nextElement.right:
                tree.append(nextElement.right)
            if nextElement.left:
                tree.append(nextElement.left)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Maintain two stacks for the two trees
        # Keep ensuring that the leafs are the same
        tree1 = [root1]
        tree2 = [root2]

        while tree1 and tree2:
            # Find the next leaf in both trees
            self.iterateTillLeaf(tree1)
            self.iterateTillLeaf(tree2)
            leaf1 = tree1.pop().val
            leaf2 = tree2.pop().val

            if leaf1 != leaf2:
                return False


        return (len(tree1) == 0 and len(tree2) == 0)