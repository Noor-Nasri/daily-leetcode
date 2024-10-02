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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool solve(ListNode* head, TreeNode* root, bool forced){
        if (head == NULL) return true;
        if (root == NULL) return false;

        // O(nodes tree): each node in tree can get called at most twice from parent
        bool works = false;
        if (head->val == root->val){ // can continue chain
            works = solve(head->next, root->left, true) || solve(head->next, root->right, true); 
        }

        if (!forced){ // can skip this node and go a layer deeper
            works = works || solve(head, root->left, false) || solve(head, root->right, false); 
        }

        return works;
    }

    bool isSubPath(ListNode* head, TreeNode* root) {
        return solve(head, root, false);
    }
};