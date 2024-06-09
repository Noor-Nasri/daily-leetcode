class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, vector<int>> targets = {};
        int solution = 0;
        int total = 0;

        for (int ind_end = 0; ind_end < nums.size(); ind_end++){
            total += nums[ind_end];
            if (total % k == 0){
                solution++;
            }

            // dist_over_k is how much we went OVER the last target
            int dist_over_last = total % k;
            int dist_to_next;
            if (total >= 0){
                dist_to_next = ((total / k + 1)*k - total)%k;
            }else{
                dist_to_next = ((total / k - 1)*k - total)%k;
            }

            if (!targets.count(dist_over_last)) targets[dist_over_last] = {};
            targets[dist_over_last].push_back(ind_end);

            // dist_to_k is how much more we have LEFT for next target
            if (dist_over_last != -dist_to_next){
                if (!targets.count(-dist_to_next)) targets[-dist_to_next] = {};
                targets[-dist_to_next].push_back(ind_end);
            }


            //cout << "Arr [0:" << ind_end << "] has total " << total << ", meaning over by " << dist_over_last << " and under by " << dist_to_next << "\n";
        }

        int prev_total = 0;
        for (int ind_start = 1; ind_start < nums.size(); ind_start++){
            prev_total += nums[ind_start - 1];
            int solves = prev_total % k;

            //cout << "Matching arr [0:" << ind_start << ") which would remove " << solves << "\n";
            if (!targets.count(solves)) continue;
            //cout << "Continuing ..\n";

            // Every element in targets[prev_total] represents an array 0:i
            // that is prev_total too much. Therefore j:i is a valid array
            vector<int>& matches = targets[solves];
            for (int target_ind = matches.size() - 1; target_ind >= 0; target_ind--){
                //cout << "Found match! " << target_ind << "\n";
                if (matches[target_ind] < ind_start) break;
                //cout << "Counted it!\n";
                solution++;
            }
        }

        return solution;
        
    }
};