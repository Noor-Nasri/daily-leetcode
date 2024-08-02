class Solution {
public:
    int minSwaps(vector<int>& nums) {
        // Very simple idea: Just pick start place of 1s
        // Then the computation can be O(1) if we know
        // - total number of 1s, and number of 1
        int total_ones = 0;
        for (int num : nums) total_ones += num;

        int num_ones = 0;
        for (int ind = 0; ind < total_ones; ind++){
            num_ones += nums[ind];
        }

        int best = total_ones - num_ones; // ind0
        for (int start_ind = 0; start_ind < nums.size() - 1; start_ind++){
            int end_ind = (start_ind + total_ones) % nums.size();
            num_ones -= nums[start_ind];
            num_ones += nums[end_ind];

            int option = total_ones - num_ones; 
            if (option < best) best = option;
        }

        return best;
    }
};