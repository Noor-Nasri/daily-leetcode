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
    tuple<ListNode*, ListNode*, int>  flipHelper(ListNode* head){
        ListNode* oldHead = head; // becomes tail
        int numElements = 1;
        ListNode* prev = head;
        ListNode* cur = head->next;
        head->next = NULL;

        while (cur != NULL){
            ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
            numElements++;
        }

        return make_tuple(prev, oldHead, numElements);
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
        tuple<ListNode*, ListNode*, int> data = flipHelper(head);
        head = shiftLeft(get<0>(data), get<1>(data), k % get<2>(data));
        head = get<0>(flipHelper(head));
    
        return head;
    }
};