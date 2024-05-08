class Solution {
public:
    int rob(vector<int>& nums) {
        int best_prev_prev = 0;
        int best_prev = nums[0];
        for (int i = 1; i < nums.size(); i++){
            int best = max(nums[i] + best_prev_prev, best_prev);
            best_prev_prev = best_prev;
            best_prev = best;
        }

        return best_prev;
    }
};