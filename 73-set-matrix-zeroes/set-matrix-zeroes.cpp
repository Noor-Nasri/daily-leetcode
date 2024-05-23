class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        // Can find PLACEHOLDER in 400^2 .. kinda dumb question
        int PLACEHOLDER = 1289612;
        int num_row = matrix.size();
        int num_col = matrix[0].size();

        for (int row = 0; row < num_row; row++){
            bool hasZero = false;
            for (int col = 0; col < num_col; col++){
                if (matrix[row][col] == 0){
                    hasZero = true;
                    break;
                }
            }

            if (!hasZero) continue;

            // set all non-0s to NULL, switch later
            for (int col = 0; col < num_col; col++){
                if (matrix[row][col] != 0){
                    matrix[row][col] = PLACEHOLDER;
                }
            }
        }

        // now repeat process for cols
        for (int col = 0; col < num_col; col++){
            bool hasZero = false;
            for (int row = 0; row < num_row; row++){
                if (matrix[row][col] == 0){
                    hasZero = true;
                    break;
                }
            }

            if (!hasZero) continue;

            // set all non-0s to NULL, switch later
            for (int row = 0; row < num_row; row++){
                if (matrix[row][col] != 0){
                    matrix[row][col] = PLACEHOLDER;
                }
            }
        }

        // now finalize
        for (int row = 0; row < num_row; row++){
            for (int col = 0; col < num_col; col++){
                if (matrix[row][col] == PLACEHOLDER) matrix[row][col] = 0;
            }
        }


    }
};