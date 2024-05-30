class Solution {
public:
    int mySqrt(int x) {
        for (int i = 1; i <= x; i++){
            long num = i;
            if (num*num > x) return i-1;
        }

        return x;
    }
};