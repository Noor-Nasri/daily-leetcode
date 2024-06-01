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
class BSTIterator {
public:
    vector<TreeNode*> nodes;
    int curPointer;
    
    void InOrderFill(TreeNode* root){
        if (root == NULL) return;
        InOrderFill(root->left);
        this->nodes.push_back(root);
        InOrderFill(root->right);
    }

    BSTIterator(TreeNode* root) {
        int test = (-1 < 0);
        this->nodes = {};
        InOrderFill(root);
        this->curPointer = -1;

    }
    
    int next() {
        this->curPointer++;
        return nodes[curPointer]->val;
    }
    
    bool hasNext() {
        if (curPointer == -1 && nodes.size()) return true; // I have NO idea why this was bugging. It should be fine ..
        return curPointer < (nodes.size() - 1);
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */