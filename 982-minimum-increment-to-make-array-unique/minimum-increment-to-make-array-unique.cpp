class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        // Greedy idea: after sorting, keep relative order the same
        // Ie, from left to right increase minimally
        
        sort(nums.begin(), nums.end());

        int totalAdjustments = 0;
        int curLargest = nums[0];

        for (int ind = 1; ind < nums.size(); ind++){
            if (nums[ind] <= curLargest){
                totalAdjustments += (curLargest - nums[ind]  + 1);
                curLargest+=1; // ie, nums[ind] is now curLargest
            }else{
                curLargest = nums[ind];
            }
        }

        return totalAdjustments;
    }
};