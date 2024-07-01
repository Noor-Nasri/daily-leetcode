class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        if (arr.size() < 2) return false;

        for (int ind = 0; ind < arr.size() - 2; ind++){
            if (arr[ind] % 2 && arr[ind+1] % 2 && arr[ind+2] % 2){
                return true;
            }
        }

        return false;
    }
};