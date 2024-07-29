class Solution {
public:
    int numTeams(vector<int>& rating) {
        int numLargerThan[rating.size()]; // num of values bigger, after this index
        int numSmallerThan[rating.size()];

        for (int ind = 0; ind < rating.size(); ind++){
            int larger = 0;
            int smaller = 0;

            for (int compare = ind + 1; compare < rating.size(); compare++){
                if (rating[compare] > rating[ind]){
                    larger++;
                }else if (rating[compare] < rating[ind]){
                    smaller++;
                }
            }

            numLargerThan[ind] = larger;
            numSmallerThan[ind] = smaller;
        }

        int total = 0;

        for (int ind1 = 0; ind1 < rating.size(); ind1++){
            for (int ind2 = ind1 + 1; ind2 < rating.size(); ind2++){
                if (rating[ind1] < rating[ind2]){
                    total += numLargerThan[ind2];
                }else if (rating[ind1] > rating[ind2]){
                    total += numSmallerThan[ind2];
                }
            }
        }

        return total;
    }
};