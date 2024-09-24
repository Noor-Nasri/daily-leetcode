#include <math.h> 
class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<int> prefixes = {};
        for (int val : arr1){
            int numdigits = ceil(log10(val + 1));

            for (int i = 0; i < numdigits; i++){
                prefixes.insert(val);
                val /= 10;
            }
        }

        int bestFind = 0;
        for (int val : arr2){
            int numdigits = ceil(log10(val + 1));

            for (int i = 0; i < numdigits; i++){
                int n = numdigits - i;

                if (n <= bestFind) break;
                if (prefixes.find(val) != prefixes.end()){
                    bestFind = n;
                }
                val /= 10;
            }
        }

        return bestFind;
    }
};