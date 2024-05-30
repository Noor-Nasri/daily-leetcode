class Solution {
public:
    int mySqrt(int x) {
        for (int i = 1; i <= x; i++){
            long num = i;
            long prod = num*num;
            if (prod > x) return i-1;
        }

        return x;
    }
};