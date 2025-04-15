class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        The question is: Which triples have the same relative ordering between nums1 and nums2?
        
        - Given a new value, everything we have seen before would be a valid [x] in that array. 
        <-->  Given a y index, everything before is an x and everything after is a z.

        - Then, if we were to get the same format for nums2: [y] = [valid x, valid z]
            - For each y, we simply get the union of the valid x and valid z lists. 
            - Then we have the valid triplets for y

        However this is n^2 (for each y, get set before and after)... how to optimize?
        .. if we were to go in order of min_index, could we reuse the list somehow?
        HINT: Divide and Conquer problem ...
        """

        index_map = {num: i for i, num in enumerate(nums2)}
  
        indices = [index_map[num] for num in nums1]

        left_counts = []
        left_sorted = SortedList()
        for idx in indices:
            left_counts.append(left_sorted.bisect_left(idx))
            left_sorted.add(idx)

        right_counts = []
        right_sorted = SortedList()
        for idx in reversed(indices):
            right_counts.append(len(right_sorted) - right_sorted.bisect_right(idx))
            right_sorted.add(idx)
        right_counts.reverse() 
        
        return sum(left * right for left, right in zip(left_counts, right_counts))

        