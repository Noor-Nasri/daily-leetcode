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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* temp = new ListNode();
        ListNode* cur_tail = temp;
        int carryOver = 0;

        while (l1 != NULL || l2 != NULL){
            int n1 = 0;
            if (l1 != NULL){
                n1 = l1->val;
                l1 = l1->next;
            }

            int n2 = 0;
            if (l2 != NULL){
                n2 = l2->val;
                l2 = l2->next;
            }
            
            int total = n1 + n2 + carryOver;
            int digit = total % 10;
            carryOver = total / 10;

            ListNode* next = new ListNode(digit);
            cur_tail->next = next;
            cur_tail = next;
        }

        if (carryOver){
            ListNode* next = new ListNode(1);
            cur_tail->next = next;
        }

        return temp->next;
    }
};