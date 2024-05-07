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
                    tuple<int, int, int> seen = make_tuple(nums[i], nums[small], nums[big]);
                    if (!found.count(seen)){
                        found.insert(seen);
                        vector<int> sol = {nums[i], nums[small], nums[big]}; 
                        results.push_back(sol);
                    }
                    small++;
                    big--;

                }else if (total < target){
                    small++;
                }else{
                    big--;
                }

            }
        }

        return results;
    }
};
