class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int tot = accumulate(skill.begin(), skill.end(), 0);
        int numTeams = skill.size() / 2;
        if (tot % numTeams != 0) return -1;

        int scorePerTeam = tot / numTeams;
        unordered_map<int, int> num_counts = {};
        long long chemistry = 0;

        for (int val : skill){
            if (val >= scorePerTeam) return -1;
            int needed = scorePerTeam - val;

            if (num_counts.find(needed) != num_counts.end()){
                chemistry += needed * val;
                num_counts[needed]--;

                if (num_counts[needed] == 0){
                    num_counts.erase(needed);
                }

            }else if (num_counts.find(val) != num_counts.end()){
                num_counts[val]++;
            }else{
                num_counts[val] = 1;
            }
        }

        if (num_counts.empty()){
            return chemistry;
        }
        return -1;        
    }
};