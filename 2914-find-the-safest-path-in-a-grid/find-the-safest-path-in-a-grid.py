class Solution:
    # So this can be quickly split into two parts
    # Part 1: Tag every cell by its cost, ie dist to nearest thief
    # To tag every cell by its cost, this would be done with BFS: layer 0 is all the thieves
    # Part 2: Run a djistra algo that follows max(cost) until it reaches the target

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        adjacencies = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        nrow, ncol = len(grid), len(grid[0])

        # phase 1: capture establishedDists: (row, col) -> min dist to thief
        curDist = 0
        curLayer = []
        establishedDists = {}
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 1:
                    curLayer.append((row, col))
                    establishedDists[(row, col)] = 0

        while curLayer:
            curDist += 1
            nextLayer = []
            for row, col in curLayer:
                for deltaR, deltaC in adjacencies:
                    newRow, newCol = row + deltaR, col + deltaC
                    node = (newRow, newCol)
                    if (0 <= newRow < nrow and 0 <= newCol < ncol and node not in establishedDists):
                        nextLayer.append(node)
                        establishedDists[node] = curDist

            curLayer = nextLayer

        # phase 2: Start at (0, 0) and take path of max(min(establishedDists in path)) until (nrow - 1, ncol - 1)
        #print(establishedDists)
        explorationNodes = [[-establishedDists[(0, 0)], 0, 0]]
        seen = set()
        while explorationNodes:
            # This is a max heap, so we do -val to use the basic minheap (hence the flip)
            flippedCurMin, row, col = heappop(explorationNodes)
            #print("Exploring best path to", row, col, "which has minDist to robbers equal to", -flippedCurMin)
            if row == nrow - 1 and col == ncol - 1:
                return -flippedCurMin

            for deltaR, deltaC in adjacencies:
                newRow, newCol = row + deltaR, col + deltaC
                node = (newRow, newCol)
                if (0 <= newRow < nrow and 0 <= newCol < ncol and node not in seen):
                    seen.add(node)
                    newCost = min(-flippedCurMin, establishedDists[node])
                    heappush(explorationNodes, (-newCost, newRow, newCol))
        
        return -1