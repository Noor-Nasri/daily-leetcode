class Solution {
public:
    // Instead of using heap with O(nlogk), I will use quick select
    // To ensure O(n), we can use the median of medians technique
    // But I think the average case is enough here, practically faster to pick random pivot

    pair<int, int> swapAround(vector<int>& nums, int left, int right, int ind){
        int val = nums[ind];
        int firstBigger = left;
        swap(nums, ind, right - 1); // Put pivot at end
        for (int cur = left; cur < right - 1; cur++){
            if (nums[cur] <= val){
                swap(nums, firstBigger, cur);
                firstBigger++;
            }
        }

        swap(nums, firstBigger, right - 1);

        // Must add case to ignore duplicates due to TLE case
        // We will augment traditional partitioning to remove duplicates chunked together
        int lastIndex = firstBigger;
        int firstIndex = firstBigger;
        while (firstIndex > 0){
            if (nums[firstIndex - 1] == val) firstIndex--;
            else break;
        }

        return {firstIndex, lastIndex}; // return index of k now
    }

    void swap(vector<int>& nums, int a, int b){
        int v = nums[a];
        nums[a] = nums[b];
        nums[b] = v;
    }

    int findKthInSub(vector<int>& nums, int k, int start, int end){
        // Find element that is at index k, if arr was sorted
        //cout << "Called " << k << ", " << start << ", " << end << '\n';

        int pivot = start + (end - start) / 3; // close enough to random ..
        int val = nums[pivot];
        pair<int, int> indices = swapAround(nums, start, end, pivot);
        //cout << "After picking " << val << " it was swapped to be  at " << indices.first << ", " << indices.second << '\n';

        if (k >= indices.first - start && k <= indices.second - start) return val;

        if (k < indices.first - start){
            // Dont need right portion
            return findKthInSub(nums, k, start, indices.first);
        }else{
            // Dont need left portion
            return findKthInSub(nums, k - (indices.second - start) - 1, indices.second + 1, end);
        }
    }

    int findKthLargest(vector<int>& nums, int k) {
        return findKthInSub(nums, nums.size() - k, 0, nums.size());
    }
};