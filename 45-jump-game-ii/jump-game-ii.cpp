class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        // Admittedly, my first approach was a simple DP solution.
        // It was accepted at about 60ms, but I saw from the discussion
        // a much better intuition

        // Idea: At each point, store the furthest you could have reached,
        // in the same number of steps as from this one.

        int nextTarget = nums[0];
        int i = 1;
        int curSteps = 1;

        while (nextTarget < nums.size() - 1){
            int maxReach = max(nums[i] + i, nums[i-1]);
            nums[i] = maxReach;
            if (i == nextTarget){
                nextTarget = maxReach;
                curSteps++;
            }
            i++;
        }

        return curSteps;
    }
};