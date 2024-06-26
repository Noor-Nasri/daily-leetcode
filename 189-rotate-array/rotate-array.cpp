class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // [1,2,3,4,5,6,7] input
        // -> [7, 6, 5 || 4, 3, 2, 1]
        // -> [5, 6, 7, 1, 2, 3, 4] output

        int cutoff = k % nums.size();
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin() + cutoff);
        reverse(nums.begin() + cutoff, nums.end());
    }
};