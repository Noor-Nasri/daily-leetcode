class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int num_matches = 0;

        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == val){
                num_matches++;
            }else if (num_matches){
                nums[i - num_matches] = nums[i];
            }
        }

        return nums.size() - num_matches;
    }
};