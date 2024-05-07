class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;

        // just binary search for mid, then first and last
        // kind of messy, could have used a helper

        int found = -1;
        while (low <= high){
            int mid = (high + low)/2;

            if (nums[mid] == target){
                found = mid;
                break;
            }else if (nums[mid] < target){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        } 

        if (found == -1) return {-1, -1};

        int high2 = found - 1;
        int lowestFound = found;
        while (low <= high2){
            int mid = (high2 + low)/2;

            if (nums[mid] == target){
                lowestFound = mid;
                high2 = mid - 1;
            }else if (nums[mid] < target){
                low = mid + 1;
            }else{
                high2 = mid - 1;
            }
        } 

        int low2 = found + 1;
        int highestFound = found;
        while (low2 <= high){
            int mid = (high + low2)/2;

            if (nums[mid] == target){
                highestFound = mid;
                low2 = mid + 1;
            }else if (nums[mid] < target){
                low2 = mid + 1;
            }else{
                high = mid - 1;
            }
        } 

        return {lowestFound, highestFound};
    }
};