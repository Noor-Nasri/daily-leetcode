# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if root == None: return []
        must_delete = set(to_delete)
        roots = []
        current_iter = [(None, root)]

        while current_iter:
            next_iter = []

            for par, node in current_iter:
                if (node == None): continue
                node_becomes = node

                if (node.val in must_delete):
                    # Remove node
                    node_becomes = None
                    if par and par.left == node: par.left = None
                    if par and par.right == node: par.right = None
                elif par == None:
                    # No parent
                    roots.append(node)
    
                next_iter.append((node_becomes, node.left))
                next_iter.append((node_becomes, node.right))
            current_iter = next_iter

        return roots
