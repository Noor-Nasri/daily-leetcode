class Solution {
public:
    int hammingWeight(int n) {
        int numOnes = 0;
        for (int i = 30; i > -1; i--){
            int cutoff = pow(2, i);
            if (n >= cutoff){
                n -= cutoff;
                numOnes++;
            }
        }

        return numOnes;
    }
};