class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // for O(1) memory, we just abuse that it appears > n/2 times
        // Count occurance of just one element, switch as it proves impossible

        int occurances = 1;
        int major_value = nums[0];

        for (int i = 1; i < nums.size(); i++){
            int new_value = nums[i];

            if (new_value == major_value){
                occurances++;
            }else{
                occurances--;

                if (!occurances){
                    occurances = 1;
                    major_value = new_value;
                }
            }
        }

        return major_value;
    }
};