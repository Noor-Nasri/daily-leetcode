class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // n^2 obv solution. Normally we would make a hashmap as we iterate, O(n)
        // But it also wants O(1) extra space usage, so we cannot use a hashmap..
        // Given that it is sorted, we can use a 2 pointer approach.

        int low = 0;
        int high = numbers.size() - 1;

        while (low < high){
            int total = numbers[low] + numbers[high];
            if (total == target){
                return {low + 1, high + 1};
            }

            if (total < target){
                low++;
            }else{
                high--;
            }
        }

        return {-1, -1};
        
    }
};