class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> money(nums.size() + 1);
        money[1] = nums[0];

        for (int i = 1; i < nums.size(); i++){
            int option = nums[i] + money[i-1];
            money[i + 1] = max(option, money[i]);
        }

        return money[nums.size()];
    }
};