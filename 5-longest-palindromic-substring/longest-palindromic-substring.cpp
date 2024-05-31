class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() < 2) return s;
        // Start off with size 1 and 2 palindromes, then keep merging upwards
        int curSize = 2;
        bool isPalindrome1[s.size()];
        bool isPalindrome2[s.size()];
        int lastFound = 1;

        // initialize
        for (int i = 0; i < s.size(); i++){
            isPalindrome1[i] = true;
            if (i < s.size() - 1 && s[i] == s[i+1]){
                isPalindrome2[i] = true;
                lastFound = 2; 
            }else{
                isPalindrome2[i] = false;
            }    
        }

        while (curSize < s.size()){
            // At least one current palindrome
            bool nextLayer[s.size()];
            for (int i = 0; i < s.size(); i++) nextLayer[i] = false;

            cout << s.size() << " " << curSize << '\n';
            for (int i = 0; i < s.size() - curSize; i++){
                //cout << i << ": " << s[i] << "=" << s[i + curSize] << ", " << isPalindrome1[i + 1] << '\n';
                if (s[i] == s[i + curSize] && isPalindrome1[i + 1]){
                    nextLayer[i] = true;
                    lastFound = curSize+1;
                    //cout << "Updated found to " << lastFound << " due to " << i << '\n';
                }
            }

            // set vars for next iteration
            curSize++;
            if (curSize - lastFound >= 2) break;
            for (int i = 0; i < s.size(); i++){
                isPalindrome1[i] = isPalindrome2[i];
                isPalindrome2[i] = nextLayer[i];
            }
        }

        // return part of longest sequence
        for (int i = 0; i < s.size(); i++){
            if (lastFound == curSize && isPalindrome2[i]
                || lastFound < curSize && isPalindrome1[i]){
                return s.substr(i, lastFound); 
            }
        }

        return "";
    }
};