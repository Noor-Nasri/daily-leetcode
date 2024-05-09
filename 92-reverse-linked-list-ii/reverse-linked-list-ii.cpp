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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (left == right) return head;
        // Find prev_left and after_right
        // flip inside then reattach

        int pos = 1;
        ListNode* beforeLeft = NULL;
        ListNode* leftNode = NULL;
        ListNode* prev = NULL;
        ListNode* cur = head;

        while (cur != NULL){
            ListNode* oldprev = prev;
            prev = cur; // prev is acc cur for this, just pointer garbage
            cur = cur->next;
    
            if (pos == left - 1){
                beforeLeft = prev;
            }else if (pos == left){
                leftNode = prev;
            } else if (pos > left){
                // Flip it
                prev->next = oldprev;

                if (pos == right){
                    // End it. 1) Attach leftNode -> next [cur]
                    leftNode->next = cur;

                    // 2) Attach beforeLeft -> this [prev]
                    if (beforeLeft == NULL){
                        return prev;
                    }
                    beforeLeft->next = prev;
                    return head;
                }
            }

            pos++;
        }

        return NULL;
    }
};