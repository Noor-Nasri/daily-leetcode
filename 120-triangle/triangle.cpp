class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        for (int j = triangle.size() - 2; j > -1; j--){
            for (int i = 0; i < triangle[j].size(); i++){
                if (triangle[j + 1][i] <= triangle[j + 1][i + 1]){
                    triangle[j][i] += triangle[j + 1][i];
                }else{
                    triangle[j][i] += triangle[j + 1][i + 1];

                }
            }
        }

        return triangle[0][0];
    }
};