class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        connections = {i : [] for i in range(1, n+1)}
        for u, v in edges:
            connections[u].append(v)
            connections[v].append(u)

        curTime = 0
        curReachable = [1]
        alreadyReachedN = 0
        alreadyVisited = {i : 0 for i in range(1, n+1)}
        alreadyVisited[1] = 1
        

        while True:
            if n in curReachable:
                if alreadyReachedN:
                    return curTime
                alreadyReachedN = True
            
            cur_colour = (curTime // change) % 2
            if cur_colour: # currently red, cannot jump yet
                rem_time = change - (curTime % change) 
                curTime += rem_time

            nextReachable = []
            seen = set()
            for node in curReachable:
                for next_node in connections[node]:
                    if not next_node in seen and alreadyVisited[next_node] < 2:
                        nextReachable.append(next_node)
                        alreadyVisited[next_node] += 1
                        seen.add(next_node)


            curReachable = nextReachable
            curTime += time
            


        