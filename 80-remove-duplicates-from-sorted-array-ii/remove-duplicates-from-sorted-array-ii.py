class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_included = 0
        last_number = None
        seen_twice = False

        for val in nums:
            if val != last_number:
                nums[num_included] = val
                seen_twice = False
                last_number = val
                num_included += 1
    
            elif not seen_twice:
                nums[num_included] = val
                seen_twice = True
                num_included += 1
        
        return num_included
