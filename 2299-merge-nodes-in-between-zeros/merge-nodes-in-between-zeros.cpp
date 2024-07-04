/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* temp = new ListNode();
        ListNode* curTail = temp;

        ListNode* curIter = head->next;
        int curSum = 0;
        while (curIter != NULL){
            if (curIter->val == 0){
                curTail->next = new ListNode(curSum);
                curTail = curTail->next;
                curSum = 0;
            }else{
                curSum += curIter->val;
            }
            curIter = curIter->next;
        }

        return temp->next;
    }
};