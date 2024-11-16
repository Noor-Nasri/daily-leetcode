class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        results = []
        for ind1 in range(len(nums) - k + 1):
            valid = True
            for ind2 in range(ind1 + 1, ind1 + k):
                if nums[ind2] != nums[ind2 - 1] + 1: 
                    valid = False
                    break
            
            results.append(valid and nums[ind1] + k-1 or -1)
        
        return results
            
        