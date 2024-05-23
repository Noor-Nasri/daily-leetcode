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
    ListNode* partition(ListNode* head, int x) {
        ListNode* less_head = new ListNode();
        ListNode* less_tail = less_head;
        ListNode* grea_head = new ListNode();
        ListNode* grea_tail = grea_head;

        ListNode* cur = head;
        while (cur != NULL){
            if (cur->val < x){
                less_tail->next = cur;
                less_tail = cur;
            }else{
                grea_tail->next = cur;
                grea_tail = cur;
            }

            cur = cur->next;
        }

        grea_tail->next = NULL;

        // now return list1, list2
        if (less_head->next == NULL) return grea_head->next;
        less_tail->next = grea_head->next;
        return less_head->next;
    }
};