class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        connections = {}
        for a, b, w in edges:
            connections[(a, b)] = w
            connections[(b, a)] = w
        
        # now the O(n^3) algo I remember from college ..
        for middle_jump in range(n):
            for start in range(n):
                for end in range(start + 1, n): # bidirectional, so all symmetric
                    if not (start, middle_jump) in connections or not (middle_jump, end) in connections:
                        continue
                    
                    # Can make a jump, check if its better than we usually have
                    dist = connections[(start, middle_jump)] + connections[(middle_jump, end)]
                    if not ((start, end) in connections) or dist < connections[(start, end)]:
                        connections[(start, end)] = dist
                        connections[(end, start)] = dist

        num_conns = [0 for i in range(n)]
        for conn in connections:
            st, en = conn
            if connections[conn] <= distanceThreshold:
                num_conns[st] += 1
        
        best_city = min(num_conns)
        for ind in range(n -1, -1, -1):
            if num_conns[ind] == best_city: return ind 
                    

