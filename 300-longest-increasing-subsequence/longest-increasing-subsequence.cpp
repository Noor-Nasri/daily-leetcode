class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // O(n^2), at each point, see which prev we can tag onto
        int best_sol = 0;
        int sol_arr[nums.size()];

        for (int j = 0; j < nums.size(); j++){
            int best_length = 1;
            for (int pred_ind = j-1 ; pred_ind > -1; pred_ind--){
                if ((nums[pred_ind] < nums[j]) && (sol_arr[pred_ind] >= best_length)){
                    best_length = sol_arr[pred_ind]+1;
                }
            }

            sol_arr[j] = best_length;
            if (sol_arr[j] > best_sol) best_sol = sol_arr[j] ;
        }

        return best_sol;
    }
};