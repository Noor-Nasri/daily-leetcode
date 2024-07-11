class Solution {
public:
    void flipHelper(string& target, int s, int e){
        int diff = e - s;
        for (int ind = 0; ind <= diff/2; ind++){
            char temp = target[s + ind];
            target[s + ind] = target[e - ind];
            target[e - ind] = temp;
        }
    }

    string reverseParentheses(string s) {
        vector<pair<int, int>> flips = {};
        stack<int> ind_opens = {};
        int count = 0;

        for (int ind= 0; ind < s.size(); ind++){
            if (s[ind] == '('){
                ind_opens.push(ind);
                count++;
            }else if (s[ind] == ')'){
                cout << ind_opens.top() << ", " << ind << '\n';
                flips.push_back({ind_opens.top(), ind});
                ind_opens.pop();
            }
        }

        for (pair<int, int> flip : flips){
            flipHelper(s, flip.first, flip.second);
        }

        int size_result = s.size() - count * 2 + 1;
        char result[size_result];
        result[size_result - 1] = '\0';

        int ind = 0;
        for (int c : s){
            if (c == '(' || c == ')') continue;
            result[ind] = c;
            ind++;
        }

        return result;
    }
};