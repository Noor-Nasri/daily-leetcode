class Solution {
public:
    int maximumRemovals(string s, string p, vector<int>& removable) {
        int low = 0;
        int high = removable.size() - 1;

        while (low <= high){
            int mid = (low + high) / 2;
            for (int ind = low; ind <= mid; ind++) s[removable[ind]] += 30;

            // check if subseq can be made
            int ind_sub = 0;
            int ind_full = 0;
            while (ind_sub < p.size() && ind_full < s.size()){
                if (s[ind_full] == p[ind_sub]) ind_sub++;
                ind_full++;
            }

            if (ind_sub == p.size()){
                // YES, can still be made
                if (mid == high) return mid + 1;
                low = mid + 1;
            }else{
                // NO, too much
                if (mid == low) return mid;
                for (int ind = low; ind <= mid; ind++) s[removable[ind]] -= 30;
                high = mid - 1;
            }


           

        }


        return -1;
    }
};