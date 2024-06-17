class Solution {
public:
    bool judgeSquareSum(int c) {
        if (c == 0) return true;
        double cutoff = pow(c, 0.5);
        for (int a = 0; a < cutoff; a++){
            double b = pow(c - pow(a, 2), 0.5);
            int int_b = b;
            if (b == int_b){ // suitable choice for b
                return true;
            }
        }

        return false;
    }
};