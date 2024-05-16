class Solution {
public:
    static bool comparator ( pair<int,int>&l, pair<int,int>& r){
        return l.first < r.first;
    }

    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        // Idea: Go through (sorted) cap until we cant, add profits to MaxHeap
        // When we can't reach the next cap, or all done, start POPing till done. 
        // If we are at k or cant do any more projects, return profits

        // first sort while storing indices
        vector<pair<int, int>> newCapitals;
        for (int i = 0; i < capital.size(); i++){
            newCapitals.push_back(make_pair(capital[i], i));
        }
        sort(newCapitals.begin(), newCapitals.end(), comparator); 
        
        // now iter
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