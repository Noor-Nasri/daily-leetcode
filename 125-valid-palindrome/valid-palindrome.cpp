class Solution {
public:
    bool isPalindrome(string s) {
        char filtered[s.size() + 1];
        int size_filtered = 0; 
        for (char c : s){
            if (c >= 'A' && c <= 'Z'){
                filtered[size_filtered] = c - 'A' + 'a';
                size_filtered++;
            }else if (c >= 'a' && c <= 'z' || c >= '0' && c <= '9' ){
                filtered[size_filtered] = c;
                size_filtered++;
            }
        }

        if (!size_filtered) return true;
        
        filtered[size_filtered] = '\0';
        int cutoff = size_filtered/2;

        for (int i = 0; i <= cutoff; i++){
            char first = filtered[i];
            char second = filtered[size_filtered - 1 - i];
            if (first != second) return false;
        }
        return true;
    }
};