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
    int searchAndPopulate(TreeNode* root, int rem_depth, vector<int>& values){
        if (root==NULL) return rem_depth;
        rem_depth--;

        if (rem_depth == 0){
            values.push_back(root->val);
            rem_depth = 1;
        }

        int rightBranchDepth = searchAndPopulate(root->right, rem_depth, values);
        int leftBranchDepth = searchAndPopulate(root->left, rightBranchDepth, values);
        return leftBranchDepth + 1;
    }

    vector<int> rightSideView(TreeNode* root) {
        vector<int> values;
        searchAndPopulate(root, 1, values);
        return values;
    }
};