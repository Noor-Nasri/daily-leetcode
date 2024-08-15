class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int billCounts[3] = {0, 0, 0};
        for (int bill : bills){
            if (bill == 5){
                billCounts[0]++;
            }else if (bill == 10){
                if (!billCounts[0]) return false;
                billCounts[0]--;
                billCounts[1]++;
            }else{
                if (billCounts[0] && billCounts[1]){
                    billCounts[0]--;
                    billCounts[1]--;
                    billCounts[2]++;
                }else if (billCounts[0] >= 3){
                    billCounts[0]-=3;
                    billCounts[2]++;
                }else{
                    return false;
                }
            }
        }

        return true;
    }
};