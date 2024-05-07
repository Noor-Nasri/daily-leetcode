class Solution {
public:
    int calculate(string s) {
        long currentValue = 0;
        long currentMultiplier = 1; // 1 for add and -1 for sub

        // for nesting brackets
        stack<long> waitingValues; 
        stack<long> waitingMultipliers; 

        for (int i = 0; i < s.size(); i++){
            char c = s[i];
    
            if (c == '+') currentMultiplier = 1;
            else if (c == '-') currentMultiplier = -1;
            else if (c == '('){
                waitingValues.push(currentValue);
                waitingMultipliers.push(currentMultiplier);
                currentValue = 0;
                currentMultiplier = 1;
            }else if (c == ')'){
                int prevValue = waitingValues.top();
                int prevMult = waitingMultipliers.top();
                currentValue = prevValue + currentValue*prevMult;

                waitingValues.pop();
                waitingMultipliers.pop();

            }else if (c >= '0' && c <= '9'){
                // Figure out current number 
                long number = c - '0';
                for (i++; i < s.size(); i++){
                    char c2 = s[i];
                    if (c2 < '0' || c2 > '9') break;

                    int digit = c2 - '0';
                    number = number*10 + digit;
                }
                i--;


                currentValue += number * currentMultiplier;
            }
        }

        return currentValue;
    }
};