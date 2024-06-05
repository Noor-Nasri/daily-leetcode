class Solution {
public:
    vector<int> lastVisitedIntegers(vector<int>& nums) {
        vector<int> seen = {};
        vector<int> answer = {};
        int num_conseq = 0;

        for (int num : nums){
            if (num == -1){
                num_conseq += 1;
                int index = seen.size() - num_conseq;
                if (index < 0){
                    answer.push_back(-1);
                }else{
                    answer.push_back(seen[index]);
                }

            }else{
                seen.push_back(num);
                num_conseq = 0;
            }
        }

        return answer;
    }
};