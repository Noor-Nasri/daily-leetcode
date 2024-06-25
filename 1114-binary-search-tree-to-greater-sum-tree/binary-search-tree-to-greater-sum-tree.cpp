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
    int adjustTree(TreeNode* root, int carryOver){
        if (root == NULL) return 0;
        int v = root->val;
        int tot_right = adjustTree(root->right, carryOver);
        root->val += tot_right;
        if (root->right == NULL){
            root->val += carryOver;
        }

        if (root->left == NULL){
            //cout << "Set value of " << v << " to " << root->val << ", due to " << carryOver <<", " << tot_right << ". Returning val as is\n";
            return root->val;
        }

        int tot_left = adjustTree(root->left, root->val);
        //cout << "Set value of " << v << " to " << root->val << ", due to " << carryOver <<", " << tot_right << ". Returning as left: " << tot_left << "\n";
        return tot_left;
        
    }

    TreeNode* bstToGst(TreeNode* root) {
        adjustTree(root, 0);
        return root;
    }
};