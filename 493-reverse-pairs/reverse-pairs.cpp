class Solution {
public:
    int sortAndCount(vector<int>& nums, int start, int end){
        // returns number of funny inversions within nums
        if (start == end) return 0;
        if (start + 1 == end){
            int num1 = nums[start];
            int num2 = nums[end];

            if (num1 > num2){
                nums[start] = num2;
                nums[end] = num1;
            }

            long prod = 2L * num2;
            if (num1 > prod) return 1; 
            return 0;
        }

        // count pairs within two sections, then add overlap
        int mid = (start+end)/2;
        int totalInversions = 0;
        totalInversions += sortAndCount(nums, start, mid-1);
        totalInversions += sortAndCount(nums, mid, end);

        int ind1 = start;
        int ind2 = mid;
        while (ind1 < mid && ind2 <= end){
            long prod = 2L * nums[ind2];
            if (nums[ind1] > prod ){
                // all items after ind1 are also pairs with ind2
                totalInversions += mid - ind1;
                ind2++;
            }else{
                // ind1 has no pairs in [ind2, end]
                ind1++;
            }
        }

        // now handle regular merge sort
        ind1 = start;
        ind2 = mid;
        vector<int> nextNums = {};
        while (ind1 < mid || ind2 <= end){
            if (ind1 == mid){
                nextNums.push_back(nums[ind2++]);
            }else if (ind2 > end){
                nextNums.push_back(nums[ind1++]);
            }else if (nums[ind1] <= nums[ind2]){
                nextNums.push_back(nums[ind1++]);
            }else{
                nextNums.push_back(nums[ind2++]);
            }
        }

        for (int ind = start; ind <= end; ind++){
            nums[ind] = nextNums[ind - start];
        }

        return totalInversions;
    }

    int reversePairs(vector<int>& nums) {
        return sortAndCount(nums, 0, nums.size() - 1);
    }
};