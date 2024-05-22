class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Arr1[i] holds best deal that ENDS <= i
        // Arr2[j] holds best deal that STARTS at >= j
        int n = prices.size();
        int arr1[n];
        arr1[0] = 0;

        int min_seen = prices[0];
        for (int i = 1; i < n; i++){
            int cur = prices[i];
            int best_deal = max(arr1[i-1], cur - min_seen);
            arr1[i] = best_deal;
            if (cur < min_seen) min_seen = cur;
        }

        int arr2[n];
        arr2[n - 1] = 0;
        int max_seen = prices[n - 1];

        for (int j = n - 2; j > -1; j--){
            int cur = prices[j];
            int best_deal = max(arr2[j+1], max_seen - cur);
            arr2[j] = best_deal;
            if (cur > max_seen) max_seen = cur;
        }

        // now simple put solution together
        int best = 0;
        for (int i = 0; i < n; i++){
            int cur = arr1[i] + arr2[i];
            if (cur > best) best = cur;
        }

        return best;
    }
};