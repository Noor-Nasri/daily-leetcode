"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return
        cur = [root] 
        # They want constant space but are okay with me doing this recursively instead?

        while (cur):
            nextIter = []
            for ind in range(len(cur)):
                node = cur[ind]
                if node.left: nextIter.append(node.left)
                if node.right: nextIter.append(node.right)
                if ind + 1< len(cur):
                    node.next = cur[ind + 1]
            
            cur = nextIter

        return root




        