from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2: return node1

        indToSeen = [{node1}, {node2}]
        indToQueue = [deque([node1]), deque([node2])]
        
        while indToQueue[0] or indToQueue[1]:
            solutions = []
            for ind in range(2):
                for _ in range(len(indToQueue[ind])):
                    node = indToQueue[ind].popleft()
                    
                    if edges[node] != -1 and edges[node] not in indToSeen[ind]:
                        indToSeen[ind].add(edges[node])
                        indToQueue[ind].append(edges[node])

                        if edges[node] in indToSeen[1 - ind]:
                            solutions.append(edges[node])
            
            if solutions:
                return min(solutions)
        
        return -1