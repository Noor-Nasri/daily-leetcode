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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL) return NULL;

        ListNode* cur = head;
        ListNode* prev = NULL;
        while (cur != NULL && cur->next != NULL){
            int val = cur->val;

            ListNode* cutoff = cur->next;
            while (cutoff != NULL && cutoff->val == val){
                cutoff = cutoff->next;
            }

            if (cutoff != cur->next){
                if (prev){
                    prev->next = cutoff;
                }else{ // this is the new head
                    head = cutoff;
                }
                cur = cutoff;

            }else{
                prev = cur;
                cur = cur->next;
            }
        }

        return head;
    }
};