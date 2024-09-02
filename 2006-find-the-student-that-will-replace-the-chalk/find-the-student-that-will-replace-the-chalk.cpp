class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long  tot = 0;
        for (int c : chalk) tot += c;

        k %= tot;
        for (int ind = 0; ind < chalk.size(); ind++){
            if (k < chalk[ind]){
                return ind;
            }

            k -= chalk[ind];
        }

        return 0;
    }
};