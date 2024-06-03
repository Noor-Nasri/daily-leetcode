class Solution {
public:
    static bool cmp(const int& a, const int& b){
        return a > b; // Flip from maxheap to minheap
    }

    int findKthLargest(vector<int>& nums, int k) {
        // Store the k largest elements, then simply return the smallest
        vector<int> minheap = {};

        // Put first k elements into the heap and heapify: O(k)
        for (int i = 0; i < k; i++){
            minheap.push_back(nums[i]);
        }
        make_heap(minheap.begin(), minheap.end(), cmp);

        // For next (n-k) elements, use heap; O(logk) each time
        for (int i = k; i < nums.size(); i++){
            if (nums[i] < minheap.front()) continue; // not in k largest

            // Remove smallest, put current
            pop_heap(minheap.begin(), minheap.end(), cmp);
            minheap.pop_back();

            minheap.push_back(nums[i]);
            push_heap(minheap.begin(), minheap.end(), cmp);
        }

        return minheap.front();
    }
};