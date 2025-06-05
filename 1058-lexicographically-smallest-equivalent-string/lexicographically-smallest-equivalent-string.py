class Solution:
    def branchConnections(self, curChar, bestChar):
        self.bestMatch[curChar] = bestChar
        for conn in self.connections[curChar]:
            if conn not in self.bestMatch:
                self.branchConnections(conn, bestChar)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Compute mapping [el] -> smallest equal element. Then just convert all.
        # To make this, first make all connections. then work upwards from a, then b, etc to connect all back.

        self.connections = {chr(e) : set() for e in range(ord('a'), ord('z') + 1)}
        for ind in range(len(s1)):
            self.connections[s1[ind]].add(s2[ind])
            self.connections[s2[ind]].add(s1[ind])
        
        self.bestMatch = {}
        for i in range(ord('a'), ord('z') + 1):
            char = chr(i)
            if char not in self.bestMatch:
                self.branchConnections(char, char)
         
        smallest = []
        for char in baseStr:
            smallest.append(self.bestMatch[char])
        
        return "".join(smallest)

        