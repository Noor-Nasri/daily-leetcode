class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() < 2) return s;
        // Start off with size 1 and 2 palindromes, then keep merging upwards
        int curSize = 2;
        bool isPalindrome1[s.size()];
        bool isPalindrome2[s.size()];
        bool nextLayer[s.size()];
        int lastFound = 1;

        // initialize
        for (int i = 0; i < s.size(); i++){
            isPalindrome1[i] = true;
            nextLayer[i] = false;
            if (i < s.size() - 1){
                if (s[i] == s[i+1]){
                    isPalindrome2[i] = true;
                    lastFound = 2; 
                }else{
                    isPalindrome2[i] = false;
                }
            }   
        }

        // Terminates when can't find palindrome in 2 conseq numbers
        while (curSize < s.size()){
            for (int i = 0; i < s.size() - curSize; i++){
                if (s[i] == s[i + curSize] && isPalindrome1[i + 1]){
                    nextLayer[i] = true;
                    lastFound = curSize+1;
                } else{
                    nextLayer[i] = false;
                }
            }

            // set vars for next iteration
            curSize++;
            if (curSize - lastFound >= 2) break;
            for (int i = 0; i < s.size() - lastFound + 1; i++){
                isPalindrome1[i] = isPalindrome2[i];
                isPalindrome2[i] = nextLayer[i];
            }
        }

        // return part of longest sequence
        for (int i = 0; i < s.size() - lastFound + 1; i++){
            if (lastFound == curSize && isPalindrome2[i]
                || lastFound < curSize && isPalindrome1[i]){
                return s.substr(i, lastFound); 
            }
        }

        return "";
    }
};