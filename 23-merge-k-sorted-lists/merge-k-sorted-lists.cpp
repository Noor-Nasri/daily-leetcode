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
    static bool cmp(const ListNode* a, const ListNode* b){
        // in regular max heap, we want true iff a < b
        // I flipped it here to instead create min heap
        return a->val > b->val;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Store current heads in min heap
        // Each time, pop top of heap and store next element in that LL
        // O(nlogk)
        // Is there O(n)?

        vector<ListNode*> curLeast;
        for (ListNode* list : lists){
            if (list == NULL) continue;
            curLeast.push_back(list);
        }
        make_heap(curLeast.begin(), curLeast.end(), cmp);


        ListNode* newHead = new ListNode();
        ListNode* newTail = newHead;

        while (!curLeast.empty()){
            // move heap head to back, then remove back
            pop_heap(curLeast.begin(), curLeast.end(), cmp); 
            ListNode* smallest = curLeast.back();
            curLeast.pop_back();

            // Now add this to the mega list
            newTail->next = smallest;
            newTail=smallest;


            if (smallest->next == NULL) continue;
            // Put next element into heap, then heapify
            curLeast.push_back(smallest->next);
            push_heap(curLeast.begin(), curLeast.end(), cmp);
            
        }

        return newHead->next; // next cuz first is placeholder

    }
};