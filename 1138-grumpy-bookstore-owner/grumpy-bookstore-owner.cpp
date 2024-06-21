class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int alreadySatisfied = 0;
        int maxAdditional = 0;
        int addSatisfied = 0;

        for (int i = 0; i < customers.size(); i++){
            if (grumpy[i]){
                addSatisfied += customers[i];
            }else{
                alreadySatisfied += customers[i];
            }

            if (i >= minutes && grumpy[i - minutes]){
                addSatisfied -= customers[i - minutes];
                // sliding window starts moving
            }

            if (addSatisfied > maxAdditional){
                maxAdditional = addSatisfied;
            }
        }

        return alreadySatisfied + maxAdditional;

        
    }
};