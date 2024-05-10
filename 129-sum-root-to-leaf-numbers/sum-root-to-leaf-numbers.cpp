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
    int sumDownwards(TreeNode* root, int total){
        total = total*10 + root->val;
        if (root->left == NULL && root->right == NULL){
            return total;
        }

        if (root->left == NULL){
            return sumDownwards(root->right, total);
        }else if (root->right == NULL){
            return sumDownwards(root->left, total);
        }

        return sumDownwards(root->left, total) + sumDownwards(root->right, total);
    }

    int sumNumbers(TreeNode* root) {
        return sumDownwards(root, 0);
    }

};