/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Base case
        if (root == NULL || root == p || root == q) return root;

        // Branching
        TreeNode* foundLeft = lowestCommonAncestor(root->left, p, q);
        TreeNode* foundRight = lowestCommonAncestor(root->right, p, q);
        
        // Found the LCA already, just return it (will be unique, no cmp needed)
        if (foundLeft != NULL && foundLeft != p && foundLeft != q) return foundLeft;
        if (foundRight != NULL && foundRight != p && foundRight != q) return foundRight;

        // no solution yet, check if this one is, or return as told
        if (foundLeft != NULL && foundRight != NULL) return root;
        if (foundLeft != NULL) return foundLeft;
        if (foundRight != NULL) return foundRight;
        return NULL;
    

    }

};