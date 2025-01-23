class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        serverCount = 0

        # None for 0, ind for 1 server, and n_max for > 1
        serversInRows = [None for i in range(n_row)]
        serversInCols = [None for i in range(n_col)]

        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col]:
                    #print("Found item at", row, col)
                    serverCount += 1
                    serversInRows[row] = (serversInRows[row] != None) and n_col or col  
                    serversInCols[col] = (serversInCols[col] != None) and n_row or row  
                    #print(serversInRows,serversInCols)
        
        #print(serversInRows)
        #print(serversInCols)
        for row in range(n_row):
            col = serversInRows[row]
            if col != None and col < n_col and serversInCols[col] == row:
                serverCount -= 1

        return serverCount

                

        