class Solution:
    # I feel like there is some weighted avg solution here
    # Lets just do BS on the line then keep counting area. log2(10**9) is only 30

    def getAreaAboveLine(self, squares, yValue):
        totalArea = 0
        for x, y, l in squares:
            hAboveLine = min(max(y + l - yValue, 0), l)
            totalArea += l * hAboveLine
        
        return totalArea

    def separateSquares(self, squares: List[List[int]]) -> float:
        targetArea = self.getAreaAboveLine(squares, 0) / 2
        print(targetArea)
        low = 0
        high = 10**9
        best = None

        while low < high - 0.00001:
            mid = (low + high)/2
            areaAbove = self.getAreaAboveLine(squares, mid)
            if targetArea >= areaAbove:
                # If we need more area, or if we are good, set this as highest solution
                high = mid
            else:
                low = mid
        
        return (low + high)/2