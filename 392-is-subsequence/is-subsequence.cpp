class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.size() == 0) return true;
        int matched = 0;

        for (char c : t){
            if (c == s[matched]){
                matched++;
                if (matched == s.size()) return true;
            }

        }

        return false;
    }
};