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
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> results(m, vector<int>(n, -1)); 
        int col = 0;
        int row = 0;

        while (m > 0 && n > 0 && head != NULL){
            if (m == 1 && n == 1 && head != NULL){
                results[row][col] = head->val;
            }
            
            // do one spiral layer, and end up with (n-2) x (m-2) for next layer
            for (int i = 0; i < n - 1; i++){ // right
                results[row][col] = head->val;
                head = head->next;
                col++;

                if (head == NULL) return results; 
            }

            for (int i = 0; i < m - 1; i++){ // down
                results[row][col] = head->val;
                head = head->next;
                row++;

                if (head == NULL) return results; 
            }

            for (int i = 0; i < n - 1; i++){ // left
                results[row][col] = head->val;
                head = head->next;
                col--;

                if (head == NULL) return results; 
            }

            for (int i = 0; i < m - 1; i++){ // up
                results[row][col] = head->val;
                head = head->next;
                row--;

                if (head == NULL) return results; 
            }

            row++;
            col++;
            m -= 2;
            n -= 2;

        }

        return results;
    }
};