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
    void pushInSortedOrder(TreeNode* root, vector<int>& sorted_values){
        if(root == NULL) return;

        pushInSortedOrder(root->left, sorted_values);
        sorted_values.push_back(root->val);
        pushInSortedOrder(root->right, sorted_values);
    }

    TreeNode* splitSorted(vector<int>& sorted_values, int low, int high){
        if(low > high) return NULL;

        int mid = (low + high)/2;
        TreeNode* newRoot = new TreeNode(sorted_values[mid]);
        newRoot->left = splitSorted(sorted_values, low, mid-1);
        newRoot->right = splitSorted(sorted_values, mid+1, high);
        return newRoot;
    }

    TreeNode* balanceBST(TreeNode* root) {
        vector<int> sorted_values = {};
        pushInSortedOrder(root, sorted_values);
        TreeNode* bst = splitSorted(sorted_values, 0, sorted_values.size() - 1);
        return bst;
    }


    

    
};