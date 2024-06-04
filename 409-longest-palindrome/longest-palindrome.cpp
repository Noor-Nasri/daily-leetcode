class Solution {
public:
    int longestPalindrome(string s) {
        if (s.size() == 0) return 0;
        int total = 0;

        unordered_set<char> seen = {};
        for (char c : s){
            if (seen.count(c)){
                total += 2;
                seen.erase(c);
            }else{
                seen.insert(c);
            }
        }

        if (seen.size()){
            total += 1;
            // Can put 1 in middle
        }
        return total;
    }
};