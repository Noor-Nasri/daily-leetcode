class Solution {
public:

    static bool comp(const pair<int, int>& first, const pair<int, int>& second){
        if (first.first < second.first) return false; // False to make it minHeap
        if (first.first == second.first && first.second > second.second) return false;
        return true;
    }

    string clearStars(string s) {
        vector<pair<int, int>> minHeap = {};
        int include[s.size()];
        int num_exclude = 0;

        for (int j = 0; j < s.size(); j++){
            char c = s[j];
            //cout << "Looking at char: " << c << '\n';

            if (c == '*'){
                num_exclude += 2;
                include[j] = 0;

                // get the next one to remove
                pop_heap(minHeap.begin(), minHeap.end(), comp);
                pair<int, int> top = minHeap.back();
                minHeap.pop_back();
                include[top.second] = 0;
                //cout << "Excluded " << top.second << " due to " << j << '\n';

            }else{
                include[j] = 1;
                minHeap.push_back({c, j});
                push_heap(minHeap.begin(), minHeap.end(), comp);
                //cout << "Current min is ind: " << minHeap.front().second << '\n'; 
            }
        }


        // reconstruct
        //cout << "Reconstructing\n";
        char newString[s.size() - num_exclude + 1];
        newString[s.size() - num_exclude] = '\0';
        int cur = 0;
        for (int i = 0; i < s.size(); i++){
            //cout << i << " is " << include[i] << '\n';
            if (!include[i]) continue;
            newString[cur] = s[i];
            //cout << "Placed it at " << cur;
            cur++;
        }

        //cout << newString << '\n';
        
        return newString;
    }
};