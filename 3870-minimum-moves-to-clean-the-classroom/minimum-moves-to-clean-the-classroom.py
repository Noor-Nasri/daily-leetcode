class Solution:
    # I see this as a classic BFS, except that you can revisit a cell if you have more energy than last time
    # So we just track [(row, col, energy)] and maintain [(row, col)] = lastVisitEnergy 
    # But maybe less energy is fine if there is less cleaning this time ...
    # Since there is at most 10 L, how about we just track (row, col, remEnergy, remLitter)
    # And we are allowed to revisit as long as we either have more energy than before or less litter
    # So total grid space is 20*20*50*10 with up to 4 adjacencies, total iteration within 1mil

    # No this isn't enough, because the variations of which Ls are left matter. 2^10 = 1024 options.
    # 20*20*50*1024 = ~20mil, so this actually still works. 
    # I cant think of a more optimized DP or greedy. Maybe some BS would work. For now 20mil okay.


    def minMoves(self, classroom: List[str], energy: int) -> int:
        adjacencies = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        nrows, ncols = len(classroom), len(classroom[0])
        litterIndFromPos = {}
        litterCount = 0
        startRow, startCol = -1, -1
        for row in range(nrows):
            for col in range(ncols):
                if classroom[row][col] == 'L':
                    litterIndFromPos[(row, col)] = litterCount
                    litterCount += 1
                elif classroom[row][col] == 'S':
                    startRow, startCol = row, col

        if litterCount == 0:
            return 0
            
        visited = {(startRow, startCol, 0): energy}
        exploreLayer = [(startRow, startCol, 0, energy)]
        targetLitter = int('1'*litterCount, 2)
        moves = 1

        while exploreLayer:
            nextLayer = []
            for row, col, missingLitter, remEnergy in exploreLayer:
                if remEnergy < visited[(row, col, missingLitter)]:
                    continue # In case same cell is added twice in a layer
                
                for dr, dc in adjacencies:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < nrows and 0 <= nc < ncols):
                        continue
                    
                    newLitter = missingLitter
                    newEnergy = remEnergy - 1
                    landingChar = classroom[nr][nc]
                    if landingChar == 'L':
                        newLitter |= (2 ** litterIndFromPos[(nr, nc)])
                        if newLitter == targetLitter:
                            return moves
                    elif landingChar == 'R':
                        newEnergy = energy
                    elif landingChar == 'X':
                        continue
                    
                    if not newEnergy:
                        continue # Wont be able to get to an R
                    
                    newInd = (nr, nc, newLitter)
                    if newEnergy <= visited.get(newInd, -1):
                        continue
                    
                    visited[newInd] = newEnergy
                    nextLayer.append((nr, nc, newLitter, newEnergy))

            exploreLayer = nextLayer
            moves += 1

        return -1



