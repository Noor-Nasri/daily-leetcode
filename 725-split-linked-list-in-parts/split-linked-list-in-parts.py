# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head

        while (cur != None):
            length += 1
            cur = cur.next
        
        if length < k:
            numEach = 1
            numWithExtras = 0
        else:
            numEach = length // k
            numWithExtras = length % k
    
        newItems = []
        newHead = None
        newTail = None
        newLength = 0
        cur = head

        while (cur != None):
            desiredLength = numEach
            if numWithExtras > 0:
                desiredLength += 1

            if newHead == None:
                newHead = cur
                newTail = cur
            else:
                newTail = cur

            newLength += 1
            cur = cur.next
            if newLength == desiredLength:
                newTail.next = None
                newItems.append(newHead)
                numWithExtras -= 1
                newHead = None
                newTail = None
                newLength = 0


        while len(newItems) < k:
            newItems.append(None)
        
        return newItems


        