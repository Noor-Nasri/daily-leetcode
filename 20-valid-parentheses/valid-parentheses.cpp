class Solution {
public:
    bool isValid(string s) {
        stack<char> curStack;
        unordered_set<char> openBrackets;
        openBrackets.insert('(');
        openBrackets.insert('[');
        openBrackets.insert('{');

        for (char c : s){
            if (openBrackets.count(c)){
                // open
                curStack.push(c);
            }else{
                // close
                if (curStack.empty()) return false;
                char old = curStack.top();
                if (
                    c == ')' && old != '(' ||
                    c == ']' && old != '[' ||
                    c == '}' && old != '{' ){
                        return false;
                    }

                curStack.pop();
            }
        }

        return curStack.empty();
    }
};