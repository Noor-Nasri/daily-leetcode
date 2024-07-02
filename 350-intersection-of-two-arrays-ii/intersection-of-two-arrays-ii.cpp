class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        int counts1[1001] = {};
        int counts2[1001] = {};
        for (int num : nums1) counts1[num]++;
        for (int num : nums2) counts2[num]++;

        vector<int> results = {};
        for (int i = 0; i < 1001; i++){
            int count = 0;
            while (count < counts1[i] && count < counts2[i]){
                count++;
                results.push_back(i);
            }
        }

        return results;
    }
};