class Solution {
public:
    int minimumDeletions(string s) {
        // first, get [i] = {num b before index, num a after index} in O(n)
        // then we can solve in O(n)
        int num_b_before_index[s.size()];
        int num_a_after_index[s.size()];
        int total_a = 0;
        int total_b = 0;

        for (int ind_b = 0; ind_b < s.size(); ind_b++){
            num_b_before_index[ind_b] = total_b;
            if (s[ind_b] == 'b') total_b++;
        }

        for (int ind_a = s.size() - 1; ind_a > -1; ind_a--){
            num_a_after_index[ind_a] = total_a;
            if (s[ind_a] == 'a') total_a++;
        }

        // now solve
        int bestOption = total_a;
        for (int ind = 0; ind < s.size(); ind++){
            if (s[ind] == 'a'){
                // Explore option of this being the last A
                int option = num_b_before_index[ind] + num_a_after_index[ind];
                if (option < bestOption){
                    bestOption = option;
                }
            }
        }

        return bestOption;
    }
};