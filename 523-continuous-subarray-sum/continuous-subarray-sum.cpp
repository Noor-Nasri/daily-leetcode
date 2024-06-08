class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        // First, make a set of all remainders based on sum(nums[:i]) for all i
        // Then when we do another runthrough, we get sum(nums[:j])
        // Want sum(nums[:i]) - sum(nums[:j]) == k

        unordered_map<int, int> all_totals = {}; // total->latest i
        int total = nums[0];
        for (int ind = 1; ind < nums.size(); ind++){
            if (nums[ind] + nums[ind-1] == 0) return true;
            total += nums[ind];
            total %= k;
            all_totals[total] = ind;
            if (total == 0) return true;
        }


        total = 0;
        for (int ind = 0; ind < nums.size() - 1; ind++){
            // Section to cut off
            total += nums[ind];
            total %= k;

            if (all_totals.count(total) && all_totals[total] >= ind + 2){
                // Ie, take the prev array and remove this start chunk
                return true;
            }
        }

        return false;
    }
};