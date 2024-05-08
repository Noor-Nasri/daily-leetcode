class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> solution;
        // This one took too long because I was trying to do math ..
        // The idea is super simple: ABC [D] EF = (ABD)x(EF)=
        // build up (ABD) then go backward to get (EF)

        int prod = 1;
        for (int num: nums){
            solution.push_back(prod);
            prod *= num;
        }

        // backward pass
        prod = 1;
        for (int i = nums.size() - 1; i >= 0; i--){
            solution[i] *= prod;
            prod *= nums[i];
        }

        return solution;
    }
};