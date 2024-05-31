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
    TreeNode* findTail(TreeNode* root){
        if (root->right == NULL) return root;
        return findTail(root->right);
    }

    void flatten(TreeNode* root) {
        if (root == NULL) return;
        TreeNode* pre_left = root->left;
        TreeNode* pre_right = root->right;

        flatten(pre_right);
        if (pre_left){
            flatten(pre_left);
            root->right = pre_left;
            root->left = NULL;
            findTail(pre_left)->right = pre_right;
        }
    }
};