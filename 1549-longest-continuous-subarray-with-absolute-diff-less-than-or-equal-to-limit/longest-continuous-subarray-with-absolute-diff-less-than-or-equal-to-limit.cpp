struct cmpHelper {
    bool operator()(const pair<int, int>& a, const pair<int, int>& b) const {
        if (a.first == b.first) return a.second < b.second;
        return a.first < b.first;
    }
};

class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        set<pair<int, int>, cmpHelper> tree = {};
        int longestArray = 1;
        int startInd = 0;

        for (int endInd = 0; endInd < nums.size(); endInd++){
            while (!tree.empty()){
                // shift startInd to the right until it fits

                int minElement = tree.begin()->first;
                int maxElement = tree.rbegin()->first;
                if (abs(nums[endInd] - minElement) > limit || abs(nums[endInd] - maxElement) > limit){
                    // remove the element in startInd

                    tree.erase({nums[startInd], startInd});
                    startInd++;
                }else{
                    break;
                }
            }

            tree.insert({nums[endInd], endInd});
            if (endInd - startInd + 1 > longestArray){
                longestArray = endInd - startInd + 1;
            }
        }

        return longestArray;
    }
};