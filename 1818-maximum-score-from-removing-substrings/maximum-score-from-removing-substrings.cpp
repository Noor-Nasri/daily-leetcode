class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int primary_bonus = max(x, y);
        int secondary_bonus = min(x, y);
        vector<char> primary;
        vector<char> secondary;

        if (x >= y){
            primary = {'a', 'b'};
            secondary = {'b', 'a'};
        } else{
            primary = {'b', 'a'};
            secondary = {'a', 'b'};
        }

        stack<pair<char, int>> prev = {};
        int total = 0;
        for (int ind = 0; ind < s.size(); ind++){
            // match all primary first
            if (!prev.empty() && prev.top().first == primary[0] && s[ind] == primary[1]){
                s[prev.top().second] = '.';
                s[ind] = '.';
                prev.pop();
                total += primary_bonus;
            }else{
                prev.push({s[ind], ind});
            }
        }

        stack<char> prev2 = {};
        for (int ind = 0; ind < s.size(); ind++){
            // now match secondary
            if (s[ind] == '.') continue;

            if (!prev2.empty() && prev2.top() == secondary[0] && s[ind] == secondary[1]){
                prev2.pop();
                total += secondary_bonus;
            }else{
                prev2.push(s[ind]);
            }
        }

        return total;
    }
};