class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        // idea 1: circular means sum(0:i) + sum (j:n) where i<=j
        // first solve with greedy (no circular), then enforce circular

        // That solution ran at 44ms (beats 64%), but then I saw another method
        // Instead of enforcing circular, notice that max_circ = total - min_arr

        // solve both with greedy, then take best
        int best_non_circ = nums[0]; // forced non-empty
        int best_minarr = 100000;

        int cur_max = 0;
        int cur_min = 0;
        int total = 0;
        for (int i = 0; i < nums.size(); i++){
            cur_max += nums[i];
            cur_min += nums[i];
            total += nums[i];

            if (cur_max > best_non_circ) best_non_circ = cur_max;
            if (cur_min < best_minarr) best_minarr = cur_min;

            if (cur_max < 0) cur_max = 0;
            if (cur_min > 0) cur_min = 0;
        }

        if (best_non_circ < 0){ 
            // all negatives edge case
            return best_non_circ;
        }

        int best_circ = total - best_minarr;
        return max(best_non_circ, best_circ);
    }
};