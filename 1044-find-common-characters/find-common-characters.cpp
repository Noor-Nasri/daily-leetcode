class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        unordered_map<char, int> min_occur = {};
        for (char c : words[0]){
            if (min_occur.count(c)) min_occur[c]++;
            else min_occur[c] = 1;
        }

        for (int ind = 1; ind < words.size(); ind++){
            unordered_map<char, int> occurs = {};
            for (char c : words[ind]){
                if (occurs.count(c)) occurs[c]++;
                else occurs[c] = 1;
            }

            for (pair<char, int> cur : min_occur){
                if (! occurs.count(cur.first)){
                    // That character doesnt exist here
                    //min_occur.erase(cur.first);
                    min_occur[cur.first] = 0;
                }else{
                    min_occur[cur.first] = min(cur.second, occurs[cur.first]);
                }
            }
        }


        vector<string> solution = {};
        for (pair<char, int> cur : min_occur){
            for (int rep = 0; rep < cur.second; rep++){
                string s;
                s += cur.first;
                solution.push_back(s);
            }
        }

        return solution;
    }
};