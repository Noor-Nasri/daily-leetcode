class Solution:
    def floodGrid(self, station, conns, stationToGridInd, curGrid):
        for connected in conns[station]:
            if connected in stationToGridInd:
                continue

            curGrid.append(connected)
            stationToGridInd[connected] = stationToGridInd[station]
            self.floodGrid(connected, conns, stationToGridInd, curGrid)

    def getGrids(self, c, connections):
        conns = [[] for i in range(c + 1)]
        for u, v in connections:
            conns[u].append(v)
            conns[v].append(u)

        grids = []
        stationToGridInd = {}
        for station in range(1, c + 1):
            if station in stationToGridInd:
                continue

            newGrid = [station]
            stationToGridInd[station] = len(grids)
            self.floodGrid(station, conns, stationToGridInd, newGrid)
            grids.append(newGrid)

        return grids, stationToGridInd
        
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        grids, stationToGridInd = self.getGrids(c, connections)
        #print(grids)
        #print(stationToGridInd)
        closedStations = set()
        grids = [sorted(e) for e in grids]
        earliestOpen = [0 for i in range(len(grids))]

        
        result = []
        for t, x in queries:
            if t == 1:
                if x in closedStations:
                    gridInd = stationToGridInd[x]
                    if earliestOpen[gridInd] == len(grids[gridInd]):
                        result.append(-1)
                    else:
                        result.append(grids[gridInd][earliestOpen[gridInd]])
                else:
                    result.append(x)
                    
            elif t == 2:
                closedStations.add(x)
                gridInd = stationToGridInd[x]
                #print("===")
                #print(closedStations)
                #print(grids[gridInd])
                #print(earliestOpen[gridInd])
                while earliestOpen[gridInd] < len(grids[gridInd]) and grids[gridInd][earliestOpen[gridInd]] in closedStations:
                    earliestOpen[gridInd] += 1


        return result

        


            