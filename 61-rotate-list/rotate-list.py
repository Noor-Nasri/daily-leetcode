# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Pretty simple, just compute the new head and move previous chain to tail
    # Writing this out, its actually a bit annoying since there are a few steps

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head
        length = 1
        while (tail.next):
            length += 1
            tail = tail.next
        
        numShifts  = k % length
        if not numShifts:
            return head
        
        newHeadInd = length - numShifts
        newTail = head
        for i in range(newHeadInd - 1):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        tail.next = head
        return newHead