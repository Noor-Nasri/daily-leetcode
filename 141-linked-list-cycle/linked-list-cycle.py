# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    MAXVAL = 10**5 + 1

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None): return False
        if (head.val == self.MAXVAL): return True

        head.val = self.MAXVAL
        return self.hasCycle(head.next)


        