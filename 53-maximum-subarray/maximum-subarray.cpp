class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int bestSums[nums.size()];
        bestSums[0] = nums[0];
        // bestSum[i] gives best option for any subarray ending here
        // best(i) = best(i - 1) + nums[i] , ie tack it on top (unless negative)

        int bestOverall = nums[0];
        for (int i = 1; i < nums.size(); i++){
            if (bestSums[i-1] > 0){
                bestSums[i] = bestSums[i-1] + nums[i];
            }else{
                bestSums[i] = nums[i];
            }

            if (bestSums[i] > bestOverall) bestOverall = bestSums[i];
        }
        
        return bestOverall;
    }
};