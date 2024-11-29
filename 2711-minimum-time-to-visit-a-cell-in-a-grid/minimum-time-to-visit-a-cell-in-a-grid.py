from heapq import heappop, heappush
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # Idea: We just need to do a shortest path. You can always stall a path by going back and forth
        # Therefore, only need to visit a node twice, once as odd and once as even

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1 # edge case of not being able to stall

        options = []
        heappush(options, (0, (0, 0)))
        goal = (len(grid)-1, len(grid[0]) - 1)
        seen = { 0 : set(), 1 : set()}
        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1]
        ]

        while options:
            t, pos = heappop(options)
            if pos in seen[t % 2]: continue
            seen[t % 2].add(pos)

            if pos == goal:
                return t
            
            for dr, dc in directions:
                npos = (pos[0] + dr, pos[1] + dc)
                if not (0 <= npos[0] < len(grid) and 0 <= npos[1] < len(grid[0])):
                    continue
                
                if t >= grid[npos[0]][npos[1]] - 1:
                    timeOfArr = t + 1
                else:
                    # Need to stall
                    timeOfArr = t + (grid[npos[0]][npos[1]] - t)//2 * 2 + 1

                if npos in seen[timeOfArr % 2]: continue

                heappush(options, (timeOfArr, npos))
    
        return -1
            



        
        