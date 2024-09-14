class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int maxNumber = 0;
        int curCount = 0;
        int highestCount = 0;

        for (int num : nums){
            if (num == maxNumber){
                curCount++;
                if (curCount > highestCount){
                    highestCount = curCount;
                }

            }else if (num > maxNumber) {
                curCount = 1;
                highestCount = 1;
                maxNumber = num;

            }else{
                curCount = 0;
            }
            
        }

        return highestCount;
        
    }
};