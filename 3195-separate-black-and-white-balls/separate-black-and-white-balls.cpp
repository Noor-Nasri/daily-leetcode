class Solution {
public:
    long long minimumSteps(string s) {
        // we want all 0s before all 1s. When we see a 0, we shift it by number of 1s to go to the left
        long long numBlack = 0;
        long long total = 0;

        for (char c : s){
            if (c == '0'){
                total += numBlack;
            }else{
                numBlack++;
            }
        }

        return total;
    }
};