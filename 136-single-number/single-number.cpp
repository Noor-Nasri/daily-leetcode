class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // can do this with BIT operations .. 
        // At every bit, a number that appears twice will result in even # of 1s
        // It will be odd iff the unique number has 1 in that bit

        int total = 0;
        for (int i = 0; i < 31; i++){
            int num1s = 0;

            for (int j = 0; j < nums.size(); j++){
                num1s += nums[j] & 1;
                nums[j] = nums[j]>>1;
            }

            if (num1s % 2 == 1){
                if (i==30){
                    return total - pow(2, 30);
                }
                
                total += pow(2, i);
            }
        }

        return total;
        
    }
};