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
    int gcd(int v1, int v2){
        for (int i = min(v1, v2); i > 0; i--){
            if ((v1 % i == 0) && (v2 % i == 0)) {

                return i;
            }
        }
        return 1;
    }

    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* temp = head;

        while (temp->next != NULL){
            ListNode* newNode = new ListNode(gcd(temp->val, temp->next->val), temp->next);
            temp->next = newNode;
            temp = temp->next->next;
        }

        return head;
    }
};