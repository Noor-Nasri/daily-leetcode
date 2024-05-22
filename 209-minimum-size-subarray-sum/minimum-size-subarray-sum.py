class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # go through, include until we have >= target
        # Then, see if we can exclude any from the left
        # Then exclude 1 more and continue trying for >= target

        left = 0
        right = 0
        tot = 0
        best = 0

        while right < len(nums):
            tot += nums[right]
            right += 1
            
            if tot >= target:
                # See if we can exclude any from left
                while (tot - nums[left] >= target):
                    tot -= nums[left]
                    left += 1
                
                num_elements = right - left
                if not best or num_elements < best:
                    best = num_elements

                # Move left up, done looking at everything before
                tot -= nums[left]
                left += 1
        
        return best
        
            
                


        