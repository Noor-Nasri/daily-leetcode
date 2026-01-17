class Solution:
    # n is only 10^3, we can just get all intersection regions between rectangles
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        maxSide = 0
        for ind1 in range(len(bottomLeft)):
            for ind2 in range(ind1 + 1, len(bottomLeft)):
                intersectBottomLeft = [max(bottomLeft[ind1][0], bottomLeft[ind2][0]), max(bottomLeft[ind1][1], bottomLeft[ind2][1])]
                intersectTopRight = [min(topRight[ind1][0], topRight[ind2][0]), min(topRight[ind1][1], topRight[ind2][1])]
                sideLength = min(intersectTopRight[0] - intersectBottomLeft[0], intersectTopRight[1] - intersectBottomLeft[1])
                maxSide = max(maxSide, sideLength)

        return maxSide**2
        