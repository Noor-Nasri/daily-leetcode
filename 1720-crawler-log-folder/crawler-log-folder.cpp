class Solution {
public:
    int minOperations(vector<string>& logs) {
        stack<string> files = {};

        for (string s : logs){
            if (s == "./") continue;
            if (s == "../"){
                if (!files.empty()){
                    files.pop();
                }
            }else{
                files.push(s);
            }
        }
        
        return files.size();
    }
};