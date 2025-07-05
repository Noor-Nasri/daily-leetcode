import bisect

class Solution:
    # If we do a heap for every pair, it'll be n^2logn. Too expensive
    # If we work our way through each pair with some weird 2 pointer, can probably do n^2
    # Is there a way to binary search these two indices?
    # If all values were POSITIVE: can keep picking mid inds, then we know that combos of (mid+, mid+) are bad

    # Easier approach after reading comments: do binary search on the actual product value.
    # Numbers are each within 10^5. So Our search is -10^10 --> 10^10
    # For each val, we get number of products <= val. This can also use BS.

    # Too much of a hassle to type rn so I am using this sol:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def F(X):
            """
            Counts how many products nums1[i]*nums2[j] are ≤ X
            """
            count = 0
            for num in nums1:
                if num > 0:
                    val = X / num
                    count += bisect.bisect_right(nums2, val)
                elif num < 0:
                    val = X / num
                    count += len(nums2) - bisect.bisect_left(nums2, val)
                else:
                    if X >= 0:
                        count += len(nums2)
                    
            return count

        # Initialize binary search bounds
        left = -10**10
        right = 10**10

        # Binary search loop
        while left <= right:
            mid = (left + right) // 2
            cnt = F(mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1

        return left
