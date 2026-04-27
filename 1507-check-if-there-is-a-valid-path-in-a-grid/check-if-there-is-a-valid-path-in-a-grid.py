class Solution:
    # This is clearly a simulation question, just follow the path and stop on cycle
    # The challenge is that the connections are funny. 

    # We should look at the streets as two edges from the center of the node.
    # Eg: St1 goes [-1, 0], [1, 0] while st3 goes [-1, 0], [0, 1].
    # For a connection to exist, both nodes need to point to each other 
    # So when a street points you to another street, you go from center to center
    
    def prefillConnections(self, grid):
        # Returns node->node connections after connecting adjacent half-roads
        streetValues = [
            # I did this as [dx, dy] which is actually [dc, dr]. Woops
            [[-1, 0], [1, 0]],
            [[0, -1], [0, 1]],
            [[-1, 0], [0, 1]],
            [[1, 0], [0, 1]],
            [[-1, 0], [0, -1]],
            [[1, 0], [0, -1]],
        ]

        oneWayStreet = {}
        connectedNodes = {}
        for row in range(self.nrow):
            for col in range(self.ncol):
                oneWayStreet[(row, col)] = set()
                connectedNodes[(row, col)] = set()
        
        for row in range(self.nrow):
            for col in range(self.ncol):
                curNode = (row, col)
                streetType = grid[row][col] - 1
                #print("==== exploring", curNode)
                for dc, dr in streetValues[streetType]:
                    connection = (row + dr, col + dc)
                    if connection not in oneWayStreet: # oob
                        #print("Non valid connection", connection)
                        continue
                    
                    #print("Valid Connection", connection)
                    if curNode in oneWayStreet[connection]:
                        connectedNodes[curNode].add(connection)
                        connectedNodes[connection].add(curNode)
                    else:
                        oneWayStreet[curNode].add(connection)
        
        return connectedNodes

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.nrow, self.ncol = len(grid), len(grid[0])
        target = (self.nrow - 1, self.ncol - 1)
        connectedNodes = self.prefillConnections(grid)
        #print(connectedNodes)

        seen = { (0, 0) }
        explore = [ (0, 0) ] # Max 2 paths based on init, but we can just do normal dfs
        while explore:
            node = explore.pop()
            if node == target:
                return True

            for conn in connectedNodes[node]:
                if conn not in seen:
                    seen.add(conn)
                    explore.append(conn)

        
        return False
        



        