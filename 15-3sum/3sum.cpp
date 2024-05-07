class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        set<tuple<int, int, int>> solutions;

        // Old python solution simplified to 2-sum n times
        // Was somehow too slow, looking into hint "2 pointer" instead of 2-sum
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
                    tuple<int, int, int> sol = make_tuple(nums[i], nums[small], nums[big]);
                    solutions.insert(sol);
                    small++;
                    big--;

                }else if (total < target){
                    small++;
                }else{
                    big--;
                }

            }
        }

        vector<vector<int>> results;
        for (tuple<int, int, int> tup : solutions){
            vector<int> solution;
            solution.push_back(get<0>(tup));
            solution.push_back(get<1>(tup));
            solution.push_back(get<2>(tup));
            results.push_back(solution);
        }
        return results;
    }
};
