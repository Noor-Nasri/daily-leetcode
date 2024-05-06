class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int totalProfit = 0;
        int buyValue = prices[0];

        for (int i = 1; i < prices.size(); i++){
            if (prices[i] < prices[i-1]){
                totalProfit += prices[i-1] - buyValue;
                buyValue = prices[i];
            }
        }

        totalProfit += prices.back() - buyValue;

        return totalProfit;
    }
};