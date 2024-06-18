class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int bestProfits[100001] = {};
        for (int ind = 0; ind < difficulty.size(); ind++){
            int diff = difficulty[ind];
            int prof = profit[ind];
            if (prof > bestProfits[diff]){
                bestProfits[diff] = prof;
            }
        }

        for (int ind = 1; ind < 100001; ind++){
            if (bestProfits[ind-1] > bestProfits[ind]){
                bestProfits[ind] = bestProfits[ind-1];
            }
        }

        int totalProfit = 0;
        for (int cap : worker){
            totalProfit += bestProfits[cap];
        }

        return totalProfit;
    }
};