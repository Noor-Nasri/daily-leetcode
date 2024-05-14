class Solution {
public:
    bool canJump(vector<int>& nums) {
        int curInd = 0;
        int lastInd = 0;
        while (lastInd < nums.size() - 1){
            if (curInd == lastInd && nums[curInd] == 0) return false;

            int nextMax = curInd + nums[curInd];
            if (nextMax > lastInd) lastInd = nextMax;

            curInd++;
        }

        return true;
    }
};