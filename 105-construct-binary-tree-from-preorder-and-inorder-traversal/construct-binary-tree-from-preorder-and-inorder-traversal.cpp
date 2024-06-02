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
    TreeNode* createChunk(
        vector<int>& preorder, int pre_start, int pre_end,
        vector<int>& inorder, int in_start, int in_end)
    {
        if (pre_start >= pre_end || in_start >= in_end) return NULL;
        TreeNode* head = new TreeNode(preorder[pre_start]);

        int offset = 0;
        while (inorder[in_start + offset] != head->val){
            offset++;
        }

        head->left = createChunk(
            preorder, pre_start+1, pre_start+1+offset, inorder, in_start, in_start + offset
        );

        head->right = createChunk(
            preorder, pre_start+1+offset, pre_end, inorder, in_start+1+offset, in_end
        );

        return head;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() == 0) return NULL;
        return createChunk(preorder, 0, preorder.size(), inorder, 0, inorder.size());
    }
};