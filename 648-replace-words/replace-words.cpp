class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        char newString[sentence.size() + 1];
        unordered_set<string> lookup(dictionary.begin(), dictionary.end()); 

        int ind_sentence = 0;
        int ind_new = 0;
        int word_start = 0;
        while (ind_sentence < sentence.size()){
            char cur = sentence[ind_sentence];
            newString[ind_new] = cur;
            ind_sentence++;
            ind_new++;

            if (cur == ' '){
                word_start = ind_sentence;
            }else{
                string cur_word = sentence.substr(word_start, ind_sentence - word_start);
                if (!lookup.count(cur_word)) continue; // no match yet

                // ignore rest of word
                while (ind_sentence < sentence.size() && sentence[ind_sentence] != ' '){
                    ind_sentence++;
                }
            }
        }

        newString[ind_new] = '\0';
        return newString;
    }
};