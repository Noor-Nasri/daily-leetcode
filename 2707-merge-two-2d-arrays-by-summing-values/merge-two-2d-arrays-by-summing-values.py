class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        ind1 = 0
        ind2 = 0

        while ind1 < len(nums1) or ind2 < len(nums2):
            if ind1 == len(nums1):
                result.append(nums2[ind2])
                ind2 += 1
            elif ind2 == len(nums2):
                result.append(nums1[ind1])
                ind1 += 1
            elif nums1[ind1][0] == nums2[ind2][0]:
                newElement = [nums1[ind1][0], nums1[ind1][1] + nums2[ind2][1]]
                result.append(newElement)
                ind1 += 1
                ind2 += 1
            elif nums1[ind1][0] < nums2[ind2][0]:
                result.append(nums1[ind1])
                ind1 += 1
            else:
                result.append(nums2[ind2])
                ind2 += 1



        return result