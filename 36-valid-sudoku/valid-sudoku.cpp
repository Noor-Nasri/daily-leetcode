class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> rows[9];
        unordered_set<char> cols[9];
        unordered_set<char> cubes[9];

        for (int row = 0; row < 9; row++){
            for (int col = 0; col < 9; col++){
                char value = board[col][row];
                if (value == '.') continue;
                int cube = row / 3 + 3 * (col / 3);

                if (rows[row].count(value)) return false;
                if (cols[col].count(value)) return false;
                if (cubes[cube].count(value)) return false;
                
                rows[row].insert(value);
                cols[col].insert(value);
                cubes[cube].insert(value);
            }
        }

        return true;
    }
};