class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;

        while (low <= high){
            int mid = (low + high)/2;
            if (nums[mid] == target) return mid;
            if (low == high){
                if (nums[mid] > target){
                    return low;
                }

                return low+1;
            }

            if (nums[mid] > target){
                if (low == high -1){
                    // we are going out of scope
                    return mid;
                }
                high = mid-1;
            }else{
                low = mid+1;
            }
        }

        // Case 1: 

        return min(low, high);
        
    }
};