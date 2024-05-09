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
    ListNode* flipHelper(ListNode* head){
        ListNode* prev = head;
        ListNode* cur = head->next;
        head->next = NULL;

        while (cur != NULL){
            ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
        }

        return prev;
    }

    ListNode* shiftLeft(ListNode* head, ListNode* tail, int numShifts){
        while (numShifts){
            tail->next = head;
            tail = head;

            head = tail->next;
            tail->next = NULL;

            numShifts--;
        }

        return head;
    }

    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL) return head;

        // Flip it, shift left, then flip back
        head = flipHelper(head);

        int numElements = 1;
        ListNode* tail = head;
        while (tail->next != NULL){
            tail = tail->next;
            numElements++;
        }
        int numShifts = k % numElements;

        head = shiftLeft(head, tail, numShifts);
        head = flipHelper(head);
    
        return head;
    }
};