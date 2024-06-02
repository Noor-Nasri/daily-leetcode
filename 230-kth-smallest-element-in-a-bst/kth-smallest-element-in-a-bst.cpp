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
    int kthSmallest(TreeNode* root, int k) {
        // When >= 0 is returned, it is the desired value
        // When < 0 is returned, it means the node is -(kth index + 1)
        // Ie smallest element returns -2
        if (root == NULL) return -1;
        int searchLeft = kthSmallest(root->left, k);

        if (searchLeft >= 0) return searchLeft; // already found
        if (k == -searchLeft) return root->val; // found

        // search right
        int rightSearch = kthSmallest(root->right, k + searchLeft);
        if (rightSearch >= 0) return rightSearch;
        
        //cout << "Currently at, " << root->val << ", found: " << searchLeft << ", " << rightSearch << '\n';
        return searchLeft + rightSearch;
    }
};