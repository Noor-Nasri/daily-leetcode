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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head == NULL) return NULL;
        int count = 0;
        ListNode* cur = head;

        while (cur != NULL){
            count++;
            cur = cur->next;
        }

        if (n == count){
            // Remove head
            return head->next;
        }

        int desired = count - n;
        cur = head;
        ListNode* prev = NULL;
        for (int i = 0; i < desired; i++){
            prev = cur;
            cur = cur->next;
        }

        prev->next = cur->next;
        return head;
    }
};