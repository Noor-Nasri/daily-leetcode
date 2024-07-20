class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        vector<vector<int>> result = {};

        for (int row = 0; row < rowSum.size(); row++){
            vector<int> nextRow = {};
            for (int col = 0; col < colSum.size(); col++){
                int maxAllowed = min(rowSum[row], colSum[col]);
                nextRow.push_back(maxAllowed);
                rowSum[row] -= maxAllowed;
                colSum[col]-= maxAllowed;
            }

            result.push_back(nextRow);
        }

        return result;
    }
};