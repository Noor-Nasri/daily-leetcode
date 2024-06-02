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
    TreeNode* construct(
        vector<int>& inorder, vector<int>& postorder, int in_start, int in_end, int post_start, int post_end
    ){
        if (in_start > in_end || post_start > post_end) return NULL;

        TreeNode* head = new TreeNode(postorder[post_end]);
        int offset = 0;

        while (inorder[in_end - offset] != head->val){
            offset++;
        }

        head->left = construct(
            inorder, postorder, 
            in_start, in_end - offset - 1,
            post_start, post_end - offset - 1
        );

        head->right = construct(
            inorder, postorder, 
            in_end - offset + 1, in_end,
            post_end - offset, post_end - 1
        );

        return head;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return construct(inorder, postorder, 0, inorder.size() - 1, 0, postorder.size() - 1);
    }
};