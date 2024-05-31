class Solution {
public:
    int findMin(vector<int>& nums) {
        if (nums[0] <= nums[nums.size() - 1]) return nums[0]; // already sorted

        int low = 1;
        int high = nums.size() - 1;

        while (low <= high){
            int mid = (low + high)/2;
            //cout << "Investigating " << low << ", " << high << '\n';

            if (nums[mid] < nums[mid - 1]){
                // Found it
                return nums[mid];
            }

            // if bigger than [0], still part of arr1
            if (nums[mid] > nums[0]){
                low = mid+1;
            }else{
                high = mid-1;
            }
        }
        
        return -1;
    }
};