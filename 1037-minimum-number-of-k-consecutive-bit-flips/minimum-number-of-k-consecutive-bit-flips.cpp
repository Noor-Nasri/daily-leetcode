class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        // Idea is simply: First 0 needs to be flipped with next ones
        // Cuz if you flip with previous values, it goes on to start and impossible
        // Track number of flips so far, so its O(n) instead of O(nk) = O(n^2)

        queue<int> flip_ends = {};
        int numFlips = 0;
        for (int i = 0; i < nums.size() - k + 1; i++){
            if (!flip_ends.empty() && flip_ends.front() == i){
                flip_ends.pop();
            }

            int flipValue = flip_ends.size() % 2;
            int curValue = nums[i];
            if (flipValue) curValue = 1 - curValue;
            if (curValue) continue;

            // Must flip next k to satisfy position i
            flip_ends.push(i + k);
            numFlips++;
        }

        // ensure last k-1 are all 1s, otherwise it was impossible
        for (int i = nums.size() - k + 1; i < nums.size(); i++){
            if (!flip_ends.empty() && flip_ends.front() == i){
                flip_ends.pop();
            }

            int flipValue = flip_ends.size() % 2;
            int curValue = nums[i];
            if (flipValue) curValue = 1 - curValue;
            if (!curValue) return -1;
        }

        return numFlips;
    }
};