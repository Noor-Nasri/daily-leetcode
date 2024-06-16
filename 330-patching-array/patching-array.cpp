class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        // This question looked very tricky, but after working it on paper
        // The trick becomes simple: If you can make [1, 3], then adding 4 means
        // You can make [1, 7]. See how far you can reach, and when there are gaps
        // simply add the next number!

        long maxReach = 0L;
        int adjustments = 0;
        int ind = 0;

        while (ind < nums.size() && maxReach < n){
            if (nums[ind] > maxReach + 1){
                // Including this makes a gap
                adjustments++;
                maxReach += maxReach + 1L;
                continue;
            }

            maxReach += nums[ind];
            ind++;
        }
        
        while (maxReach < n){
            adjustments++;
            maxReach += maxReach + 1L;
        }

        return adjustments;
    }
};