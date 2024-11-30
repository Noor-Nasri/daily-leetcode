class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # We can treat pairs like node connections, and we just need to use all edges
        # The algo is simply: Do DFS, then at the end backtrack. Just know the edges you took.
        # Abuse the fact that solution is garenteed: the graph is connected.
        # Case 1: There is a node with more exits than entrances. Then it must be the start
        # Case 2: They all have the same number of entrances and exits. Start anywhere.
        # For the middle, they must have the same number of enter/exits.
        # So when we go out, we know we will come back (except for the route reaching the end)

        nodeConnections_in = {}
        nodeConnections_out = {}
        for u, v in pairs:
            if not u in nodeConnections_out:
                nodeConnections_out[u] = []
            nodeConnections_out[u].append(v)

            
            if not v in nodeConnections_in:
                nodeConnections_in[v] = []
            nodeConnections_in[v].append(u)
        
        for u in nodeConnections_out:
            startingPoint = u
            num_in = u in nodeConnections_in and len(nodeConnections_in[u]) or 0
            if len(nodeConnections_out[u]) > num_in:
                break
        
        # Build the path BACKWARDS. 
        checkpoints = []
        cur = [startingPoint]

        while cur:
            # We are at this node. Now take all the exits. They will lead us back
            while cur[-1] in nodeConnections_out and nodeConnections_out[cur[-1]]:
                curPoint = cur[-1]
                nextPoint = nodeConnections_out[curPoint].pop()
                cur.append(nextPoint)
            
            # Reached a point which doesnt go any further. Thats the end, add it.
            # In the next iteration, we will be at the node that led us to this end
            endOfChain = cur.pop()
            checkpoints.append(endOfChain)

        answer = []
        for ind in range(len(checkpoints) - 2, -1, -1):
            answer.append([checkpoints[ind + 1], checkpoints[ind]])

        return answer
        
        


        
