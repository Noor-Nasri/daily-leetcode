class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int target = *max_element(nums.begin(), nums.end());
        int curCount = 0;
        int highestCount = 0;

        for (int num : nums){
            if (num == target){
                curCount++;
            }else{
                curCount = 0;
            }

            if (curCount > highestCount){
                highestCount = curCount;
            }
        }

        return highestCount;
        
    }
};