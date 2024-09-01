class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        if (original.size() != m*n) return {};
        vector<vector<int>> newArray = {};
        int ind = 0;

        for (int row = 0; row < m; row++){
            vector<int> newRow = {};

            for (int col = 0; col < n; col++){
                newRow.push_back(original[ind++]);
            }
            newArray.push_back(newRow);
        }
        
        return newArray;
    }
};