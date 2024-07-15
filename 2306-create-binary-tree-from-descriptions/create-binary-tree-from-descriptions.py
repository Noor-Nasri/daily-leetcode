# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {} 
        possible_roots = set() 

        for par, child, isLeft in descriptions:
            if not (par in nodes):
                nodes[par] = TreeNode(par)
                possible_roots.add(par)
            
            if not (child in nodes):
                nodes[child] = TreeNode(child)
            
            if isLeft:
                nodes[par].left = nodes[child]
            else:
                nodes[par].right = nodes[child]

            if child in possible_roots:
                possible_roots.remove(child)
        
        return nodes[possible_roots.pop()]