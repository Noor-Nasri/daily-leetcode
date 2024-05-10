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
    void undoLastReverse(ListNode* actualHead, ListNode* actualTail){
        // At the moment; head <--> next <- next <- next .. <- tail
        // Flip from tail until head to get back to head -> .. -> tail
        ListNode* prev = NULL;
        ListNode* cur = actualTail;

        while (cur != actualHead){
            ListNode* nex = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nex;
        }
    }

    ListNode* reverseOneGroup(ListNode* head, int k){
        // Returns NEW HEAD after flipping first k. 
        // Note that to jump k elements, just remember head argument, since it shifts k.
        // if k runs out, it will undo and return NULL
        int i = 1;

        ListNode* prev = head;
        ListNode* cur = head->next;

        while (i < k){
            if (cur == NULL){
                // We have run out of flips at the end! Must undo last flip
                undoLastReverse(head, prev);
                return NULL;
            }

            ListNode* nex = cur->next;
            cur->next = prev;

            prev = cur;
            cur = nex;
            i++;
        }

        // original head is now tail -> points to cur, which is next
        head->next = cur;
        return prev;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* initCall = reverseOneGroup(head, k);

        ListNode* curTail = head;
        while (curTail->next != NULL){
            ListNode* nextTail = curTail->next;
            ListNode* newHead = reverseOneGroup(nextTail, k);

            if (newHead == NULL){
                return initCall;
            }

            curTail->next = newHead;
            curTail = nextTail;
        }

        return initCall;
    }
};