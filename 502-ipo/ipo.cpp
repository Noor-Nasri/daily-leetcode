class Solution {
public:
    static bool comparator ( pair<int,int>&l, pair<int,int>& r){
        return l.first < r.first;
    }

    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        // Loop: Maximize capital as much as possible 
        // Logic: Of ALL CAP < cur budget: Take max profit, repeat

        // Have two sorted arrays <-> cap and profit
        // Go through cap until we cant, every time add profit to MaxHeap
        // When we can't reach the remaining cap (or all unlocked), POP. 
        // If we are at k, return cur profit

        vector<pair<int, int>> newCapitals;
        for (int i = 0; i < capital.size(); i++){
            newCapitals.push_back(make_pair(capital[i], i));
        }

        

        sort(newCapitals.begin(), newCapitals.end(), comparator); 
        
        priority_queue<int> best_profits;
        int totalProfit = w;
        int used = 0;

        for (int i = 0 ; i < newCapitals.size(); i++){
            int capRequired = newCapitals[i].first;

            while ((capRequired > totalProfit) && (used < k)){
                if (best_profits.empty()) return totalProfit; // out of options
                // take the best off of heap
                totalProfit += best_profits.top();
                best_profits.pop();
                used++;
            }

            if (used == k) return totalProfit;
            best_profits.push(profits[newCapitals[i].second]);
        }

        // use remaining ones
        while (used < k  && !best_profits.empty()){
            // take best off of heap
            totalProfit += best_profits.top();
            best_profits.pop();
            used++;
        }

        return totalProfit;
    }
};