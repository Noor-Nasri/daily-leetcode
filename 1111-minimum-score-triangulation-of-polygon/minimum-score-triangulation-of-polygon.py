class Solution:
    # Okay, this wording really confused me. First I tried just matching values (ie all with smallest two), then making good triangles.
    # They want a full subdivision of a regular polygon into triangles. 

    # The idea is: We start with all 1..n vertices. We can then take the first two vertices, and choose any other one to make triangle 1.
    # By making this triangle, we split the polygon into two polygons!  2..x and x..1
    # So just a DP that takes the current range, and tries every vert against the first two. 

    # But what if it doesn't subdivide, but instead takes out a section? Now we have to allow all verts except the middle chunk. How can we represent this?
    # Instead, provide the solve the subdivision line and the remaining range. Then, the solution must build on the subdivision line!
    # This is because no triangle can latch onto a point along the border line, so we know a triangle must be on the border!

    # So, O(n) inside of (lineP1, lineP2, remPointsStart, remPointsEnd) -> n^5. Ouch.
    # But its not actually n^5, because lineP1/P2 will be limited by the remPoints and overlap. So its secretly closer to n^3.
    # We can probably switch P1, P2 to be some bools and make it clearly n^3, but this is easier. Just trust ig


    # ^^ All that was my thinking at the time. I didn't end up having time to finish the question.
    # Using a public solution and moving on before I go on vacation
    def __init__(self):
        self.dp = [[0] * 50 for _ in range(50)]
        
    def minScoreTriangulation(self, values, i=0, j=0, res=0):
        if j == 0:
            j = len(values) - 1
        if self.dp[i][j] != 0:
            return self.dp[i][j]
        for k in range(i + 1, j):
            res = min(res if res != 0 else float('inf'),
                self.minScoreTriangulation(values, i, k) +
                values[i] * values[k] * values[j] +
                self.minScoreTriangulation(values, k, j))
        self.dp[i][j] = res
        return self.dp[i][j]