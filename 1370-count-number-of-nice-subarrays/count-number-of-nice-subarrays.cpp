class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        vector<int> odd_positions = {};
        for (int ind = 0; ind < nums.size(); ind++){
            if (nums[ind] % 2 == 1){
                odd_positions.push_back(ind);
            }
        }

        if (odd_positions.size() < k) return 0;

        // Main subarray will have exactly k odds inside
        // Can shift start and end to include extra evens
        int total = 0;
        for (int first_odd = 0; first_odd <= odd_positions.size() - k; first_odd++){
            int prev_cutoff = (first_odd > 0) ? odd_positions[first_odd - 1] : -1;
            int next_cutoff =  nums.size();
            if (first_odd + k <= odd_positions.size() - 1){
                next_cutoff = odd_positions[first_odd + k];
            }

            int possible_starts = odd_positions[first_odd] - prev_cutoff;
            int possible_ends = next_cutoff - odd_positions[first_odd + k - 1];
            total += possible_starts * possible_ends;
        }

        return total;
    }
};