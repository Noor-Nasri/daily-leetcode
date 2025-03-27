class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = {}
        dominantElement = [-1, 0]
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
            if counts[num] > dominantElement[1]:
                dominantElement = [num, counts[num]]
        
        seenDoms = 0
        remainingDoms = dominantElement[1]
        for cutoff in range(len(nums) - 1):
            if nums[cutoff] == dominantElement[0]:
                seenDoms += 1
                remainingDoms -= 1
            
            if seenDoms > (cutoff + 1)/2 and remainingDoms > (len(nums) - cutoff - 1)/2:
                return cutoff

        return -1
        
