class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long tot = 0;
        int smallestVal = 100001;
        int numNegs = 0;

        for (vector<int>& arr : matrix){
            for (int v : arr){
                tot += abs(v);
                if (v < 0){
                    numNegs++;
                    
                }

                if (abs(v) < smallestVal){ 
                    smallestVal = abs(v);
                }
            }
        }

        return (numNegs % 2 ? tot - smallestVal*2 : tot);
    
    }
};