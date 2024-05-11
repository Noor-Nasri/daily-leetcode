class Solution {
public:
    int binarySearch(vector<int>& nums, int target, int s, int e){
        while (s <= e){
            int m = (s+e)/2;

            if (nums[m] == target) return m;
            if (nums[m] < target){
                s = m+1;
            }else{
                e = m-1;
            }
        }

        return -1;
    }

    int search(vector<int>& nums, int target) {
        if (nums.size() == 1){
            if (target == nums[0]) return 0;
            return -1;
        }

        if (nums[0] < nums[nums.size() - 1]){
            // not rotated
            return binarySearch(nums, target, 0, nums.size()-1);
        }

        // find switch point
        int init = nums[0];
        int s = 0;
        int e = nums.size() -1;
        int m = 0;

        while (s <= e){
            m = (s+e)/2;

            if (nums[m] > nums[m+1]){
                // Found cutoff
                break;
            }

            if (nums[m] >= init){
                // Part of list 1
                s = m+1;
            }else{
                // Part of list 2
                e = m-1;
            }

        }

        if  (target >= init && target <= nums[m]){
            return binarySearch(nums, target, 0, m);

        }else if (target >= nums[m+1] && target <= nums[nums.size()-1]){
            return binarySearch(nums, target, m+1, nums.size()-1);
        }

        return -1;
    }
};