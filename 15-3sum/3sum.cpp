class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        set<tuple<int, int, int>> found;
        vector<vector<int>> results;
    
        // Old python solution simplified to 2-sum n times
        // Was somehow too slow, looking into hint "2 pointer" instead of hash
        for (int i = 0; i < nums.size() - 2; i++){
            // Idea: fix num1 to be at i
            // Need to get other 2 = -num1. Start at smallest + biggest
            // Shift smallest and biggest when sum > or < 0
            
            int target = -nums[i];
            int small = i+1;
            int big = nums.size() - 1;

            while (small < big){
                int total = nums[small] + nums[big];

                if (total == target){
                    // add solution
                    vector<int> sol = {nums[i], nums[small], nums[big]}; 
                    results.push_back(sol);

                    // avoid duplicates
                    while (small < nums.size()-1 && nums[small] == nums[small+1]) small++;
                    while (big > small && nums[big] == nums[big-1]) big--;
                    small++;
                    big--;

                }else if (total < target){
                    small++;
                }else{
                    big--;
                }
            }

            // avoid duplicates again
            while (i < nums.size()-1 && nums[i] == nums[i+1]) i++;
        }

        return results;
    }
};
