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
    ListNode* sortList(ListNode* head) {
        if (head == NULL) return NULL;
        // given that its LL, bubble sort is applicable
        // For nlogn, we can first get a count, then merge each half, then do double pointer
        int count = 0;
        ListNode* cur = head;

        while (cur != NULL){
            cur = cur->next;
            count++;
        }

        if (count == 1) return head;
        if (count == 2){
            // sort these 2 nodes
            if (head->val <= head->next->val) return head;

            ListNode* second = head->next;
            second->next = head;
            head->next = NULL;
            return second;
        }

        // split into 2 halves
        cur = head;
        int target = count / 2 - 1;
        
        while (target > 0){
            cur = cur->next;
            target--;
        }

        ListNode* second = cur->next;
        cur->next = NULL;

        // sort both halves
        ListNode* newFirst = sortList(head);
        ListNode* newSecond = sortList(second);
        // Now merge
        ListNode* placeHolder = new ListNode();
        ListNode* sortedTail =  placeHolder;

        while ((newFirst != NULL) || (newSecond != NULL)){

            if ((newFirst == NULL) || newSecond != NULL && (newSecond->val <= newFirst->val)){
                // Put from the second list
                sortedTail->next = newSecond;
                sortedTail = newSecond;
                newSecond = newSecond->next;

            }else{
                // Put from the first list
                sortedTail->next = newFirst;
                sortedTail = newFirst;
                newFirst = newFirst->next;
            }
            
            sortedTail->next = NULL;
        }

        return placeHolder->next;

    }
};