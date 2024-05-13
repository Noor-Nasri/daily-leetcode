class Solution {
public:
    int climbStairs(int n) {
        if (n==1) return 1;
        if (n==2) return 2;

        int prev = 1;
        int cur = 2;

        for (int i = 3; i < n ; i++){
            int sol = prev + cur;
            prev = cur;
            cur = sol;
        }

        return prev + cur;
    }
};