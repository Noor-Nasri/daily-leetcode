class TreeNode2{
public:
    string word;
    TreeNode2* left;
    TreeNode2* right;

    TreeNode2(string word){
        this->word = word;
        this->left = NULL;
        this->right = NULL;
    }

};


class Trie {
public:
    TreeNode2* root;
    Trie() {
        this->root = NULL;
    }
    
    bool traverse(string word, TreeNode2* root, int mode){
        if (root == NULL) return false;

        bool isMatch;
        if (mode < 2){
            isMatch = word == root->word;
        }else{
            isMatch = root->word.rfind(word, 0) == 0; // search just start of woor word
        }

        if (isMatch) return true;

        TreeNode2* childNode = (word > root->word) ? root->right : root->left;
        bool foundLater = traverse(word, childNode, mode);

        if (!foundLater && mode == 0){
            // Should insert it
            foundLater = true;
            TreeNode2* newNode = new TreeNode2(word);
            
            if (word > root->word){
                root->right = newNode;
            }else{
                root->left = newNode;
            }
        }

        return foundLater;
    }

    void insert(string word) {
        if (this->root == NULL){
            this->root = new TreeNode2(word);
        }else{
            traverse(word, this->root, 0);
        }

    }
    
    bool search(string word) {
        return traverse(word, this->root, 1);
    }
    
    bool startsWith(string prefix) {
        return traverse(prefix, this->root, 2);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */