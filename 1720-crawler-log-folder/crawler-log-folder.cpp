class Solution {
public:
    int minOperations(vector<string>& logs) {
        int depth = 0;

        for (string s : logs){
            if (s == "./") continue;
            if (s != "../"){
                depth++;
            }else if (depth > 0){
                depth--;
            }
        }
        
        return depth;
    }
};