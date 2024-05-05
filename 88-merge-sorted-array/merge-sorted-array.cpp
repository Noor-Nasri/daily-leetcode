class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // build it backwards to avoid extra memory
        int ind_new = m + n - 1;
        int ind_1 = m - 1;
        int ind_2 = n - 1;

        while (ind_new >= 0){
            if (ind_2 == -1 || ind_1 >= 0 && nums1[ind_1] >= nums2[ind_2]){
                nums1[ind_new] = nums1[ind_1];
                ind_1--;
            }else{
                nums1[ind_new] = nums2[ind_2];
                ind_2--;
            }

            ind_new--;
        }

    }
};