class Solution {
public:
    int hammingWeight(int n) {
        /*
        int numOnes = 0;
        for (int i = 30; i > -1; i--){
            int cutoff = pow(2, i);
            if (n >= cutoff){
                n -= cutoff;
                numOnes++;
            }
        }

        return numOnes;
        */

        // Above solution ran at 0ms, now looking at bitwise for fun
        // Turned out super easy, just check is LSB is 1 then shift
        int numOnes = 0;
        while (n){
            numOnes += (n & 1);
            n >>= 1;
        }
        return numOnes;
    }
};