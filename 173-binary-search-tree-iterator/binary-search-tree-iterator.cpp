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
        cout << "Added " << root->val << " to nodes \n";
        InOrderFill(root->right);
    }

    BSTIterator(TreeNode* root) {
        int test = (-1 < 0);
        cout << test << '\n';

        this->nodes = {};
        InOrderFill(root);
        this->curPointer = -1;

    }
    
    int next() {
        this->curPointer++;
        return nodes[curPointer]->val;
    }
    
    bool hasNext() {
        if (curPointer == -1 && nodes.size()) return true;
        cout << curPointer << '\n';
        cout << "While we have " << nodes.size() << " elements\n";
        if (curPointer < (nodes.size() - 1)){
            return true;
        }

        cout << "Not enough room";
        return false;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */