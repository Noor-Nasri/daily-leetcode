class Solution {
public:
    static bool cmp(const vector<int>& a, const vector<int>& b){
        return a[0] > b[0]; // min heap based on sum
    }
    
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        // Idea: Start at (0,0)
        // The next choice is either (0,1) or (1,0). Also consider (1,1)
        // When (0,1) is picked, make it (0, 2) and keep picking best
        // When (1,1) is picked, we introduce (1, 2), (2, 1), (2, 2) and continue
        // This way, we use a priority queue with hopefully limited items


        vector<vector<int>> pairs;

        // Options data: sum, ind in nums1, ind in nums2, and direction
        // direction tells us which arr pointer we are moving
        vector<vector<int>> bestOptions = {{nums1[0] + nums2[0], 0, 0, 0}}; 
        make_heap(bestOptions.begin(), bestOptions.end(), cmp);


        for (int i = 0; i < k; i++){
            // Take best option
            pop_heap(bestOptions.begin(), bestOptions.end(), cmp);        
            vector<int> choice = bestOptions.back();
            pairs.push_back({nums1[choice[1]], nums2[choice[2]]});
            bestOptions.pop_back();

            // Add next options
            if (choice[1] == choice[2]){
                // Add another layer of pointers
                if (choice[2] < nums2.size() - 1){
                    vector<int> newChoice = {
                        nums1[choice[1]] + nums2[choice[2] + 1], choice[1], choice[2] + 1, 2
                        };
                    bestOptions.push_back(newChoice);
                    push_heap(bestOptions.begin(), bestOptions.end(), cmp); 
                } 

                if (choice[1] < nums1.size() - 1){
                    vector<int> newChoice = {
                        nums1[choice[1] + 1] + nums2[choice[2]], choice[1] + 1, choice[2], 1
                        };
                    bestOptions.push_back(newChoice);
                    push_heap(bestOptions.begin(), bestOptions.end(), cmp); 
                }

                if (choice[1] < nums1.size() - 1 && choice[2] < nums2.size() - 1){
                    // This one wont be picked for a while, but its waiting to be min
                    vector<int> newChoice = {
                        nums1[choice[1] + 1] + nums2[choice[2] + 1], choice[1] + 1, choice[2] + 1, 0
                        };
                    bestOptions.push_back(newChoice);
                    push_heap(bestOptions.begin(), bestOptions.end(), cmp); 
                }

            }else{
                choice[choice[3]] += 1; // Move in direction
                if (choice[3] == 1 && nums1.size() == choice[1]) continue;
                if (choice[3] == 2 && nums2.size() == choice[2]) continue;

                choice[0] = nums1[choice[1]] + nums2[choice[2]];
                bestOptions.push_back(choice);
                push_heap(bestOptions.begin(), bestOptions.end(), cmp);
            }
        }

        return pairs;
    }
};