class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> occurances;

        for (int num : nums){
            if (occurances.find(num) == occurances.end()){
                occurances[num] = 1;
            }else{
                occurances[num]++;
            }

            if (occurances[num] > nums.size()/2){
                return num;
            }
        }

        return -1;
    }
};