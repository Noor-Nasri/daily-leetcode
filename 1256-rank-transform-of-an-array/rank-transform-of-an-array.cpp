class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> keys = {};
        unordered_map<int, vector<int>> indices = {};

        for (int i = 0; i < arr.size(); i++){
            if (indices.find(arr[i]) == indices.end()){
                keys.push_back(arr[i]);
                indices[arr[i]] = {i};
            }else{
                indices[arr[i]].push_back(i);
            }
        }

        sort(keys.begin(), keys.end());
        vector<int> results(arr.size(), 0);

        for (int i = 0; i < keys.size(); i++){
            for (int ind : indices[keys[i]]){
                results[ind] = i + 1;
            }
        }
        
        return results;
    }
};