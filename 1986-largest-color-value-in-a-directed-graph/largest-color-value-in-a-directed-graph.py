class Solution:
    def solveDPForFixedColor(self, nodeInd, parentInd):
        # Node can be called with multiple parents, but it should never go back to them
        # So the answer in DP is just based on the nodeInd
        if nodeInd in self.curSolving:
            return -1

        if nodeInd in self.sols:
            return self.sols[nodeInd]

        maxFound = 0
        self.curSolving.add(nodeInd)
        for conn in self.connections[nodeInd]:
            option = self.solveDPForFixedColor(conn, nodeInd)
            if option == -1:
                return -1
            elif option > maxFound:
                maxFound = option
        
        if self.colors[nodeInd] == self.curColor:
            maxFound += 1

        self.sols[nodeInd] = maxFound
        self.curSolving.remove(nodeInd)
        return self.sols[nodeInd]


    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Split this question to 26 questions: longest path per letter
        # Directed, acyclic graph. So just go through all nodes as potential starts,
        # and use DP to store answers.
        connections = [[] for ind in range(len(colors))]
        for u, v in edges:
            connections[u].append(v)

        self.connections = connections
        self.colors = colors

        maxPath = 0
        for curColor in set(colors):
            self.curColor = curColor
            self.sols = {}
            self.curSolving = set()
            
            for startNode in range(len(colors)):
                print("")
                option = self.solveDPForFixedColor(startNode, None)
                if option == -1:
                    return -1
                elif option > maxPath:
                    maxPath = option

        return maxPath
            