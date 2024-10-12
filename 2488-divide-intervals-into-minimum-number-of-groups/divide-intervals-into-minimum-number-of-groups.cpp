class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        int times[1000002] = {};

        for (vector<int> & vals : intervals){
            times[vals[0]]++;
            times[vals[1] + 1]--;
        }

        // prefix sums?
        int tot = 0;
        int best = 0;
        for (int v : times){
            tot += v;
            if (tot > best){
                best = tot;
            }
        }

        return best;
    }
};