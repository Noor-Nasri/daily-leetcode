# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        vals = set(nums)

        while (head != None and head.val in vals):
            head = head.next
        
        prev = head
        cur = head.next

        while (cur != None):
            if (cur.val in vals):
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next


        
        return head
        