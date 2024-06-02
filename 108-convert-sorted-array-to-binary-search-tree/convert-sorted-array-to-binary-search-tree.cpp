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
    TreeNode* createBSTinCutoff(vector<int>& nums, int s, int e) {
        if (s > e) return NULL;
        int m = (s + e)/2;
        TreeNode* left = createBSTinCutoff(nums, s, m-1);
        TreeNode* right = createBSTinCutoff(nums, m+1, e);
        return new TreeNode(nums[m], left, right);;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return createBSTinCutoff(nums, 0, nums.size() - 1);
    }
};