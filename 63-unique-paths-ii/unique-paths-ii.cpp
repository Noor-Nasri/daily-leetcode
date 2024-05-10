class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int nrows = obstacleGrid.size();
        int ncols = obstacleGrid[0].size();
        int numPaths[nrows][ncols];
        if (obstacleGrid[0][0] == 1) return 0;

        numPaths[0][0] = 1;

        for (int i = 0; i < nrows; i++){
            for (int j = 0; j < ncols; j++){
                if (i==0 && j==0) continue;
                if (obstacleGrid[i][j] == 1){
                    numPaths[i][j] = 0;
                    continue;
                }
                int pathsAbove = i>0 ? numPaths[i-1][j] : 0;
                int pathsBefore = j>0 ? numPaths[i][j-1] : 0;
                numPaths[i][j] = pathsAbove + pathsBefore;
            }
        }

        return numPaths[nrows - 1][ncols - 1];
    }
};