class Solution:
    def addNum(self, num):
        if not num in self.values:
            self.values[num] = 1
        else:
            self.values[num] += 1
        self.min_val = min(self.min_val, num)
        self.max_val = max(self.max_val, num)

    def removeNum(self, num):
        self.values[num] -= 1
        if self.values[num]: return
    
        del self.values[num]
        cur_vals = list(self.values.keys()) # at most 3 keys
        self.min_val = min(cur_vals)
        self.max_val = max(cur_vals)

    def continuousSubarrays(self, nums: List[int]) -> int:
        self.values = {nums[0] : 1}
        self.min_val = nums[0]
        self.max_val = nums[0]

        total = 0
        start = 0
        end = 1

        while end < len(nums):
            self.addNum(nums[end])
            while self.max_val - self.min_val > 2:
                # move start pointer until this is valid
                # each time, include all arrs that start at start
                total += end - start
                self.removeNum(nums[start])
                start += 1

            end += 1
        
        # all combos start -> end are valid
        len_valid = end - start
        total += len_valid * (len_valid + 1) / 2 
        return int(total)