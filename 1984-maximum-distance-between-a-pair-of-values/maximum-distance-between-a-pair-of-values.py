class Solution:
    # Both arrays are sorted. Lets say we found a valid (i_1, j_1) then looked at nums1[i_1 + 1]
    # We know that any value j < j_1 that has nums1[i_1 + 1] <= nums2[j] would have also been valid for nums1[i] <= [i + 1]
    # That means, we dont need to consider any smaller values for j.
    # So this becomes a simple 2 pointer. As we move i, we move j as far up as possible while considering distance
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxDist = 0
        indJ = 0

        for indI in range(len(nums1)):
            indJ = max(indJ, indI + 1)
            while indJ < len(nums2) and nums1[indI] <= nums2[indJ]:
                maxDist = max(maxDist, indJ - indI)
                indJ += 1

        return maxDist
        