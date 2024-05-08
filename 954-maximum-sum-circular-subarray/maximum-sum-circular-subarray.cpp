class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        // idea is simple: circular means sum(0:i) + sum (j:n) where i<=j
        // first solve with greedy (no circular), then enforce circular

        // greedy for non-circ: just count best and reset when needed
        int n = nums.size();
        int best_non_circ = nums[0];
        int cur = 0;
        for (int i = 0; i < n; i++){
            cur += nums[i];
            if (cur > best_non_circ) best_non_circ = cur;
            if (cur < 0) cur = 0;
        }

        if (best_non_circ < 0){ // all negatives edge case
            return best_non_circ;
        }

        // now circular: store greedy for both directions then combine
        int best_until[n];
        int best_from[n];
        best_until[0] = nums[0]; // non-empty
        best_from[n-1] = nums[n-1];
        int total_forward = nums[0];
        int total_backward = nums[n-1];

        for (int i = 1; i < n; i++){
            total_forward += nums[i];
            total_backward += nums[n - 1 - i];

            best_until[i] = max(best_until[i-1], total_forward);
            best_from[n - 1 - i] = max(best_from[n - i], total_backward);
        }

        // combine the arrays
        int best_circ = 0;
        for (int i = 0; i < n - 2; i++){
            int option = best_until[i] + best_from[i + 2];
            if (option > best_circ) best_circ = option;
        }

        return max(best_circ, best_non_circ);
    }
};