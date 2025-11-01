class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # make every number as small as possible
        nums = sorted(nums)
        unique_vals = set()

        for num in nums:
            s = num - k
            e = num + k
            best = None
            
            while s <= e:
                m = (s + e) // 2
                if m not in unique_vals:
                    best = m
                    e = m - 1
                else:
                    # this value is taken by a smaller number. so all prev numbers are bad
                    s = m + 1

            if best != None:
                unique_vals.add(best)

        return len(unique_vals)
            
        
        