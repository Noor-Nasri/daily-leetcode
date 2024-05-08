class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> solution(nums.size());
        // This one took too long because I was trying to do math ..
        // The idea is super simple: ABC [D] EF = (ABD)x(EF)=
        // build up (ABD) then go backward to get (EF)
        solution[0] = 1;
        for (int i = 1; i < nums.size(); i++){
            solution[i] = solution[i-1] * nums[i-1];
        }

        // backward pass
        int prod = 1;
        for (int i = nums.size() - 1; i > -1; i--){
            solution[i] *= prod;
            prod *= nums[i];
        }

        return solution;
    }
};