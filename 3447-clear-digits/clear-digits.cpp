class Solution {
public:
    string clearDigits(string s) {
        stack<int> nondigits = {};
        bool keep[s.size()];
        for (int i = 0; i < s.size(); i++) keep[i] = true;

        for (int ind = 0; ind < s.size(); ind++){
            char chr = s[ind];
            if (chr >= '0' && chr <= '9'){
                keep[ind] = false;
                if (!nondigits.empty()){
                    keep[nondigits.top()] = false;
                    nondigits.pop();
                }
            }else{
                nondigits.push(ind);
            }
        }


        char newString[s.size() + 1];
        int newInd = 0;
        for (int i = 0; i < s.size(); i++){
            if (keep[i]){
                newString[newInd] = s[i];
                newInd++;
            }
        }

        newString[newInd] = '\0';
        return newString;
    }
};