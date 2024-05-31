class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() < 2) return s;
        // Start off with size 1 and 2 palindromes, then keep merging upwards
        int curSize = 2;
        int isPalindrome1[s.size()];
        int isPalindrome2[s.size()];
        int lastFound = 1;

        // initialize
        for (int i = 0; i < s.size(); i++){
            isPalindrome1[i] = 1;
            if (i < s.size() - 1 && s[i] == s[i+1]){
                isPalindrome2[i] = 1;
                lastFound = 2; 
            }else{
                isPalindrome2[i] = 0;
            }    
        }

        while (curSize < s.size()){
            // At least one current palindrome
            int nextLayer[s.size()];
            for (int i = 0; i < s.size(); i++) nextLayer[i] = 0;

            //cout << s.size() << " " << curSize << '\n';
            for (int i = 0; i < s.size() - curSize; i++){
                //cout << i << ": " << s[i] << "=" << s[i + curSize] << ", " << isPalindrome1[i + 1] << '\n';
                if (s[i] == s[i + curSize] && isPalindrome1[i + 1]){
                    nextLayer[i] = 1;
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