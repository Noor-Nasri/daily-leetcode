class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int costs[grid[0].size()];
    
        // first row option is just RIGHT
        int tot = 0;
        for (int i = 0; i<grid[0].size(); i++){
            tot += grid[0][i];
            costs[i] = tot;
        }

        for (int row=1; row < grid.size(); row++){
            costs[0] += grid[row][0]; // result of DOWN

            for (int col = 1; col < grid[row].size(); col++){
                costs[col] = grid[row][col] + min(costs[col-1], costs[col]);
            }
            
        }

        return costs[grid[0].size()-1];
    }
};