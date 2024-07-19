class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int minRow[rows];
        int maxCols[cols];

        for (int j = 0; j < rows; j++) minRow[j] = 100000;
        for (int j = 0; j < cols; j++) maxCols[j] = 0;

        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++){
                int val = matrix[row][col];

                if (val < minRow[row]) minRow[row] = val;
                if (val > maxCols[col]) maxCols[col] = val;
            }
        }

        vector<int> results = {};
        
        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++){
                int val = matrix[row][col];

                if (val == minRow[row] && val == maxCols[col]){
                    results.push_back(val);
                }
            }
        }

        return results;
    }
};