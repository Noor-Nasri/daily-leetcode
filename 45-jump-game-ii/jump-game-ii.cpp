class Solution {
public:
    int jump(vector<int>& nums) {
        int numJumps[nums.size()];
        numJumps[nums.size() - 1] = 0; 

        for (int i = nums.size() - 2 ; i > -1 ; i--){
            int best_jump_val = 100000;
            int max_jump_ind = i + nums[i];
            if (nums.size() <= max_jump_ind) max_jump_ind = nums.size() - 1;

            for (int j = i + 1; j <= max_jump_ind; j++){
                if (numJumps[j] < best_jump_val) best_jump_val = numJumps[j];
            }

            numJumps[i] = best_jump_val + 1;
        }

        return numJumps[0];
    }
};