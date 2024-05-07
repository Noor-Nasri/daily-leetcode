class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int amounts[amount + 1];

        amounts[0] = 0;
        for (int a = 1; a < amount + 1; a++){
            int bestCase = 10000000;

            for (int coin : coins){
                int remaining = a - coin;
                if (remaining < 0) continue;
                int num_coins = amounts[remaining];

                if (num_coins > -1 && num_coins < bestCase){
                    bestCase = num_coins;
                }
            }

            if (bestCase == 10000000){
                amounts[a] = -1;
            }else{
                amounts[a] = bestCase + 1;
            }
        }

        return amounts[amount];
    }
};