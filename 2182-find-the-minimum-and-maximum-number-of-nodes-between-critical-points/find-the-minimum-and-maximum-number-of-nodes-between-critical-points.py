# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # My first instinct is to just make this a list, but we don't even need to track all points
    # Just sweep for critical points and maintain min/max dist by comparing each point to prev

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prevNode, curNode = head, head.next
        firstFound, lastFound = None, None
        solution = [-1, -1]
        curInd = 1

        while curNode:
            nextNode = curNode.next
            isMax, isMin = False, False

            if nextNode:
                isMax = prevNode.val < curNode.val and nextNode.val < curNode.val
                isMin = prevNode.val > curNode.val and nextNode.val > curNode.val

            if isMax or isMin:
                if not firstFound:
                    firstFound = curInd
                else:
                    dist = curInd - lastFound
                    if solution[0] == -1:
                        solution = [dist, dist]
                    else:
                        solution[0] = min(solution[0], dist)
                        solution[1] = curInd - firstFound

                lastFound = curInd

            prevNode = curNode
            curNode = nextNode
            curInd += 1
        
        return solution