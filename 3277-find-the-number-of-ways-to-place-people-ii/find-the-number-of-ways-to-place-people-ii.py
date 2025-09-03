class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Okay, so this is just yesterdays question but it needs to be faster than n^3
        # We can take point A and B in a sorted arr, knowing all points between A and B are a fit for X
        # Therefore, we just need to see if the points have any Y in the range, breaking our rect

        # If for every pair, we have a sorted Y arr, then we can do binary search given the pair...
        # We can generate all these sorted Ys in O(n^2). Is this really the best way?
        # At every point, we can iterate backwards while maintaining the lowest Y above so far. 
        # Then, any point that is lower is acceptable!

        points = sorted(points, key = lambda x : (x[0], -x[1]))
        total = 0
        for indB in range(1, len(points)):
            _, By = points[indB]
            yCutoff = float('inf')
            for indA in range(indB - 1, -1, -1):
                _, Ay = points[indA]
                if Ay >= By and Ay < yCutoff:
                    total += 1
                    yCutoff = Ay

        return total