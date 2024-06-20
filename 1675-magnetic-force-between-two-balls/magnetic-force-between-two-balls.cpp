class Solution {
public:
    bool canSolve(vector<int>& position, int m, int min_dist){
        int rem = m - 1;
        int earliest = position[0] + min_dist;
        int ind = 1;

        while (rem > 0 && ind < position.size()){
            if (position[ind] >= earliest){
                rem--;
                earliest = position[ind] + min_dist;
            }
            ind++;
        }

        return rem==0;
    }


    int maxDistance(vector<int>& position, int m) {
        // Idea: for a specific <min dist>, can check solution in O(n)
        // Just put ball in earliest and skip the next <dist>, continue
        // Combine this with binary search, it is O(nlogm). Sort is O(nlogn)

        sort(position.begin(), position.end());
        int low = 1;
        int high = position[position.size()-1] - position[0];

        while (low <= high){
            int mid = (low + high + 1)/2;

            if (canSolve(position, m, mid)){
                if (mid == high){
                    return mid;
                }

                low = mid; // try to go higher
            }else{
                high = mid - 1; // mid couldnt work so all > impossible
            }
        }

        return -1;
    }
};