class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int s1_len = strs[0].size();
        for (int i = 0; i < s1_len; i++){
            char s1_char = strs[0][i];
            for (int j = 1; j < strs.size(); j++){
                if (strs[j][i] != s1_char){
                    return strs[0].substr(0, i);
                }
            }
        }

        return strs[0];
    }
};