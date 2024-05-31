"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def splitGrid(self, grid, rowStart, rowEnd, colStart, colEnd):
        value = grid[rowStart][colStart]
        for row in range(rowStart, rowEnd):
            for col in range(colStart, colEnd):
                if grid[row][col] == value: continue

                # Must subdivide!
                midRow = (rowStart + rowEnd) // 2
                midCol = (colStart + colEnd) // 2
                topLeft = self.splitGrid(grid, rowStart, midRow, colStart, midCol)
                topRight = self.splitGrid(grid, rowStart, midRow, midCol, colEnd)
                bottomLeft = self.splitGrid(grid, midRow, rowEnd, colStart, midCol)
                bottomRight = self.splitGrid(grid, midRow, rowEnd, midCol, colEnd)
                return Node(2, False, topLeft, topRight, bottomLeft, bottomRight)

        # All the same value
        return Node(value, True, None, None, None, None)

    def construct(self, grid: List[List[int]] ) -> 'Node':
        return self.splitGrid(grid, 0, len(grid), 0, len(grid[0]))

        