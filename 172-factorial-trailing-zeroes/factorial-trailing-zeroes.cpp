class Solution {
public:
    int trailingZeroes(int n) {
        // explanation: Every 5x2 = 10
        // A lot more 2s than 5s, so just count the 5s
        // When you have a square (25), you get 2
        int tot = 0;
        for (int i = 1; i < 7; i++){
            tot += n / pow(5, i);
        }

        return tot;
    }
};