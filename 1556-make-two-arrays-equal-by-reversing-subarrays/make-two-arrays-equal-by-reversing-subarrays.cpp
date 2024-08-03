class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        unordered_map<int, int> counts = {};
        for (int val : target){
            if (counts.find(val) == counts.end()){
                counts[val] = 1;
            }else{
                counts[val]++;
            }
        }

        for (int val : arr){
            if (counts.find(val) == counts.end()){
                return false;
            }else{
                counts[val]--;
            }
        }

        for (pair<int, int> vals : counts){
            if (vals.second != 0) return false;
        }

        return true; 
    }
};