class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        // before adjusting, it is 0/1
        // If dead-> alive, make it -1
        // If alive->dead, make it 2
        // Determine cur alive by >= 1
        
        int n_row =  board.size();
        int n_col = board[0].size();
        for (int i = 0; i < n_row; i++){
            for (int j = 0; j < n_col; j++){
                int totNeighbours = 0;
                // up/down
                if (i > 0) totNeighbours += (board[i-1][j] >= 1);
                if (i < n_row - 1) totNeighbours += (board[i+1][j] >= 1);

                // left/right
                if (j > 0) totNeighbours += (board[i][j-1] >= 1);
                if (j < n_col - 1) totNeighbours += (board[i][j+1] >= 1);
                
                // diag
                if (i > 0 && j > 0) totNeighbours += (board[i-1][j-1] >= 1);
                if (i > 0 && j < n_col - 1) totNeighbours += (board[i-1][j+1] >= 1);
                if (i < n_row - 1 && j < n_col - 1) totNeighbours += (board[i+1][j+1] >= 1);
                if (i < n_row - 1 && j > 0) totNeighbours += (board[i+1][j-1] >= 1);


                // now apply rules
                if (board[i][j] == 0){
                    // see if it should live
                    if (totNeighbours == 3) board[i][j] = -1;
                }else{
                    if (totNeighbours < 2 || totNeighbours > 3) board[i][j] = 2;
                }
            }
        } 

        for (int i = 0; i < n_row; i++){
            for (int j = 0; j < n_col; j++){
                if (board[i][j] == -1) board[i][j] = 1;
                else if (board[i][j] == 2) board[i][j] = 0;
            }
        }
    }
};