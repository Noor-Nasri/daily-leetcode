class Solution {
public:
    int hIndex(vector<int>& citations) {
        int num_sites[1001] = {};
        for (int c : citations){
            num_sites[c]++;
        }

        for (int j = 1000; j > -1; j--){
            if (num_sites[j] >= j) return j;

            num_sites[j-1] += num_sites[j];
        }

        return -1;
    }
};