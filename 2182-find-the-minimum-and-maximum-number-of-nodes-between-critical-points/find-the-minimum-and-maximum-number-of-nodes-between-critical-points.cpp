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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        if (head == NULL || head->next == NULL) return {-1, -1};
    
        ListNode* cur = head->next;
        ListNode* prev = head;
        int curIndex = 1;
        int firstSeen = -1;
        int lastSeen = -1;
        int minDist = 100001;

        while (cur->next != NULL){
            if (
                (cur->val > prev->val && cur->val > cur->next->val) ||
                (cur->val < prev->val && cur->val < cur->next->val)
                ){
                
                if (firstSeen == -1){
                    firstSeen = curIndex;
                }else if (curIndex - lastSeen < minDist){
                    minDist = curIndex - lastSeen;
                }
                lastSeen = curIndex;
            }

            prev = cur;
            cur = cur->next;
            curIndex++;
        }


        if (firstSeen == -1 || firstSeen == lastSeen) return {-1, -1};
        return {minDist, lastSeen - firstSeen};        
    }
};