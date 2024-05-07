class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> values;

        for (string s : tokens){
            if (s == "+" || s == "-" || s == "*" || s == "/"){
                int second = values.top();
                values.pop();
                int first = values.top();
                values.pop();

                if (s == "+") values.push(first + second);
                else if (s == "-") values.push(first - second);
                else if (s == "/") values.push(first / second);
                else values.push(first * second);
            }else{
                values.push(stoi(s));
            }
        }

        return values.top();
    }
};