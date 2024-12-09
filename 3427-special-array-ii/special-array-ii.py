class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # store number of problematic pairs from 0->i for each i
        # Then can solve for num of problemati pairs i->j

        problematic = [0]
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                problematic.append(problematic[-1] + 1)
            else:
                problematic.append(problematic[-1])
        
        results = []
        for a, b in queries:
            results.append(not bool(problematic[b] - problematic[a]))

        return results
        