class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        tallest_from_right = [None for _ in range(n)]
        tallest_R = -1

        for ind in range(n - 1, -1, -1):
            tallest_R = max(tallest_R, height[ind])
            tallest_from_right[ind] = tallest_R
        
        total = 0
        tallest_from_left = height[0]
        for ind in range(1, n - 1):
            val = height[ind]
            fill = min(tallest_from_left, tallest_from_right[ind + 1])
            if val < fill:
                total += fill - val
            tallest_from_left = max(val, tallest_from_left)
        return total
        

        