class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        tallest_from_left = [-1 for _ in range(n)]
        tallest_from_right = [-1 for _ in range(n)]
        tallest_L = 0
        tallest_R = 0

        for ind in range(n):
            tallest_L = max(height[ind], tallest_L)
            tallest_R = max(height[n - 1 - ind], tallest_R)

            tallest_from_left[ind] = tallest_L
            tallest_from_right[n - 1 - ind] = tallest_R
        
        total = 0
        for ind in range(1, n - 1):
            val = height[ind]
            fill = min(tallest_from_left[ind - 1], tallest_from_right[ind + 1])
            if val < fill:
                total += fill - val

        return total
        

        