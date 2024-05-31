"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: return None

        # Map each old memory ID to a new element, then fix pointers
        mappings = {} 
        temp = head
        while temp != None:
            mappings[temp] = Node(temp.val)
            temp = temp.next
        mappings[None] = None

        newHead = mappings[head]
        temp = head
        while temp != None:
            mappings[temp].next = mappings[temp.next]
            mappings[temp].random = mappings[temp.random]
            temp = temp.next

        
        return newHead
        
        