class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int bestSale = 0;
        int lowestBuy = prices[0];

        for (int i = 1; i < prices.size(); i++){
            int price = prices[i];
            if (price < lowestBuy){
                lowestBuy = price;
            }

            int sale = price - lowestBuy;
            if (sale > bestSale){
                bestSale = sale;
            }
        }

        return bestSale;

    }
};