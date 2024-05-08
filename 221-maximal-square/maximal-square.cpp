class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();

        int bestOptions[n][m];
        int bestOverall = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (matrix[i][j] == '0'){
                    bestOptions[i][j] = 0;
                    continue;
                }

                int optionLeft = 0;
                if (j > 0) optionLeft = bestOptions[i][j-1];

                int optionUp = 0;
                if (i > 0) optionUp = bestOptions[i-1][j];

                if (optionLeft != optionUp){
                    bestOptions[i][j] = min(optionLeft, optionUp) + 1;
                }else{
                    
                    // if above and prev are same length, we can make a bigger cube
                    // iff the last square before it is also filled in
                    if (i - optionUp >= 0 && j - optionLeft >= 0 && 
                    matrix[i - optionUp][j - optionLeft] == '1'){
                        bestOptions[i][j] = optionUp + 1;
                        if (bestOptions[i][j] > bestOverall){
                            bestOverall = bestOptions[i][j];
                        }
                    }else{
                        bestOptions[i][j] = optionUp ;
                    }
                }
            }
        }


        return bestOverall*bestOverall;
    }
};