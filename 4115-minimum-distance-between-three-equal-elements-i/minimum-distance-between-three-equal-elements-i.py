class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minDist = 1000000
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    continue
                
                for k in range(j + 1, len(nums)):
                    if nums[k] != nums[j]:
                        continue
                    
                    dist = 2*(k - i)
                    minDist = min(minDist, dist)
                    break
        
        if minDist == 1000000:
            return -1
        return minDist