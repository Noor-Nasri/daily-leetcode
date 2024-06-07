class TrieNode {
    // I just want the record to show .. python hashmap took like 60seconds to code
    // and worked just fine. No one needs this much optimization ...

public:
    TrieNode* children[26];
    bool isLeaf;

    TrieNode(){
        isLeaf = false;
        for (int i = 0; i < 26; i++) children[i] = NULL;
    }

    void insertWord(string& word, int curInd){
        if (word.size() == curInd){
            isLeaf = true;
            return ;
        }

        char targetChar = word[curInd];
        int childInd = (targetChar - 'a');

        if (children[childInd] == NULL){
            children[childInd] = new TrieNode();
        }

        children[childInd]->insertWord(word, curInd + 1);
    }

};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        char newString[sentence.size() + 1];
        TrieNode* root_node = new TrieNode();
        for (int i = 0; i < dictionary.size(); i++){
            root_node->insertWord(dictionary[i], 0);
        }

        
        TrieNode* cur_node = root_node;
        int ind_sentence = 0;
        int ind_new = 0;
        while (ind_sentence < sentence.size()){
            char cur = sentence[ind_sentence];
            // cout << "Currently at " << ind_sentence << " char: " << cur << "\n";

            newString[ind_new] = cur;
            ind_sentence++;
            ind_new++;

            if (cur == ' '){
                cur_node = root_node;
                // cout << "Reset root\n";
                continue;
            }

            cur_node = cur_node->children[cur - 'a'];

            if (cur_node == NULL){
                // no root found for this word, copy it all
                // cout << "Copying whole word\n";
                while (ind_sentence < sentence.size() && sentence[ind_sentence] != ' '){
                    newString[ind_new] = sentence[ind_sentence];
                    ind_sentence++;
                    ind_new++;
                }

            }else if (cur_node->isLeaf){
                // found a root, skip the rest
                // cout << "Skipping remaining word\n";
                while (ind_sentence < sentence.size() && sentence[ind_sentence] != ' ') ind_sentence++;
            }

        
        }

        newString[ind_new] = '\0';
        return newString;
    }
};