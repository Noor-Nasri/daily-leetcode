class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> counts = {};
        for (string s : arr){
            if (counts.find(s) == counts.end()){
                counts[s] = 1;
            }else{
                counts[s]++;
            }
        }

        for (string s : arr){
            if (counts[s] > 1) continue;
            k --;
            if (k == 0) return s;
        } 
        
        return "";
    }
};