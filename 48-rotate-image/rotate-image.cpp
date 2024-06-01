class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int numLayers = n / 2;

        // Do one 'layer', ie border, at a time
        for (int layer = 0; layer < numLayers; layer++ ){
            for (int ind = layer; ind < n - layer - 1; ind++){
                // Flip these 4 numbers in place
                int original = matrix[layer][ind];
                matrix[layer][ind] = matrix[n - 1 - ind][layer];
                matrix[n - 1 - ind][layer] = matrix[n - 1 - layer][n - 1 - ind];
                matrix[n - 1 - layer][n - 1 - ind] = matrix[ind][n - 1 - layer];
                matrix[ind][n - 1 - layer] = original;

            }
        }


    }
};