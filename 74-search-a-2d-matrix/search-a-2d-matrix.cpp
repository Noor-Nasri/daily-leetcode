class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int numRows = matrix.size();
        int numCols = matrix[0].size(); // size of row

        int low = 0;
        int high = numRows*numCols - 1;

        while (low <= high){
            int mid = (low + high)/2;
            int value = matrix[mid / numCols][mid % numCols];
            
            if (value == target) return true;
            else if (value < target) low = mid+1;
            else high = mid - 1;
            
        }

        return false;
    }
};