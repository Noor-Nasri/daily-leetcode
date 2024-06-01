class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        if (k == 1) {
            vector<vector<int>> sols = {};
            for (int j = 1; j <=n; j++){
                sols.push_back({j});
            }
            return sols;
        };

        vector<vector<int>> sols = {};
        vector<vector<int>> considering = {};

        for (int j = 1; j <= n; j++){
            vector<vector<int>> nextIter = {};

            for (vector<int> values : considering){
                nextIter.push_back(values); // Opt 1: Dont include

                vector<int> values2 = values;
                values2.push_back(j); // Opt2: Include

                if (values2.size() == k){

                    sols.push_back(values2);
                }else{

                    nextIter.push_back(values2);
                }
            }

            nextIter.push_back({j});
            considering = nextIter;
        }

        return sols;
    }
};