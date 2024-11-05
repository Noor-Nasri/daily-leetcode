class Solution {
public:
    int minChanges(string s) {
        int changes = 0;
        int count = 0;
        char mode = '2';

        for (char c : s){
            if (mode == c){
                count++;
            }else{
                if (count % 2 == 1){
                    // there is odd number before this, so we must change this
                    count++;
                    changes++;
                }else{
                    // can break off
                    mode = c;
                    count = 1;
                }
            }
        }

        // cant have odd here because we only split on even, and total is even. 
        return changes;
    }
};