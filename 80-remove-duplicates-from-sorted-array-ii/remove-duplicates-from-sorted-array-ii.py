class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_included = 0
        last_number = None
        seen_once = True

        for val in nums:
            if val != last_number:
                nums[num_included] = val
                seen_once = True
                last_number = val
                num_included += 1
    
            elif seen_once:
                nums[num_included] = val
                seen_once = False
                num_included += 1
        
        return num_included
