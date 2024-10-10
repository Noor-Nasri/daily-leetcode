class Solution:
    def binSearch(self, starts, num):
        # find biggest (LEFT MOST) element <= num. Items sorted in decreasing order
        low = 0
        high = len(starts)

        while (low <= high):
            mid = (low + high) // 2
            val, ind = starts[mid]

            if val > num:
                low = mid + 1
            
            else:
                if low == mid:
                    # the lowest we can go!
                    return ind

                high = mid

        return -1



    def maxWidthRamp(self, nums: List[int]) -> int:
        possible_starts = [(nums[0], 0)]
        smallest = nums[0]
        width = 0

        for ind in range(1, len(nums)):
            if nums[ind] < smallest:
                possible_starts.append((nums[ind], ind))
                smallest = nums[ind]
                continue
            
            # we have nums[ind] >= at least one element
            # we want to take earliest ind possible
            # it is possible if nums[i] <= nums[ind]
            ramp_start = self.binSearch(possible_starts, nums[ind])
            if (ind - ramp_start) > width:
                width = ind - ramp_start
        
        return width
        

