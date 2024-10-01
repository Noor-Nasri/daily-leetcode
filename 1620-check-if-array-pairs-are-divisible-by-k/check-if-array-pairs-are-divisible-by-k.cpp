class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> requiredPairings(k, 0);

        for (int val : arr){
            if (val < 0){
                val = k + (val % k); // -4 -> 2 at k=3, becomes it needs (+1) to make a pairing
            }
            int rem = val % k;

            if (requiredPairings[rem]){
                // this value can be paired with a previous value
                requiredPairings[rem]--;

            }else{
                // this value must be paired with something else
                int pairRequirement = (k - rem) % k; // 0 stays as 0, rest gets flipped 
                requiredPairings[pairRequirement]++;
            }
        }

        // check if we have unpaired elements
        for (int val : requiredPairings){
            if (val) return false;
        }

        return true;
    }
};