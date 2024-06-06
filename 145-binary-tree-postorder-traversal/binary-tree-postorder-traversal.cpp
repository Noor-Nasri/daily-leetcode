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
    void fill(TreeNode* root, vector<int>& vals) {
        if (root == NULL) return;
        fill(root->left, vals);
        fill(root->right, vals);
        vals.push_back(root->val);
    }

    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> solution = {};
        fill(root, solution);
        return solution;
    }
};