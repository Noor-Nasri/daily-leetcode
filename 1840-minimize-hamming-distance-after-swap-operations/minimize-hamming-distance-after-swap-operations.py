class Solution:
    # First thing to note: If there is a chain connecting a and b, we can just consider this as a<->b
    # Because we can swap all the way right then swap b all the way back, and everything else stays.
    # So now: when is swapping useful? Only when both elements get fixed!
    # Is there ever a choice for swapping a,b or a,c where we must choose correctly?
    # Maybe a can use both b,c but then d needs to connect with just c.

    # How can we solve this without n^2?? Even flattening connections will take more ..
    # I shamefully looked at the hint and realized I'm losing my edge ...
    # This is a simple component question. We can rearrange components as we please!
    # So just count the occurances within the components - inconsistencies can't be solved!

    def solveGroups(self, connections):
        visited = set()
        groups = []

        for ind in range(len(connections)):
            if ind in visited:
                continue

            nextGroup = [ind]
            inGroupQueue = [ind]
            visited.add(ind)

            while inGroupQueue:
                includedInd = inGroupQueue.pop()
                for conn in connections[includedInd]:
                    if conn not in visited:
                        visited.add(conn)
                        inGroupQueue.append(conn)
                        nextGroup.append(conn)

            groups.append(nextGroup)
        
        return groups

    def countNumsInGroup(self, indList, values):
        occurs = {}
        for ind in indList:
            val = values[ind]
            occurs[val] = occurs.get(val, 0) + 1
        
        return occurs
    
    def getOccuranceDiff(self, occurMap1, occurMap2):
        # We are assuming the maps have the same number of elements here
        totalElements = 0
        matched = 0
        for val in occurMap1:
            totalElements += occurMap1[val]
            matched += min(occurMap1[val], occurMap2.get(val, 0))

        return totalElements - matched

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        connections = [set() for i in range(len(source))]
        for a, b in allowedSwaps:
            connections[a].add(b)
            connections[b].add(a)

        groups = self.solveGroups(connections)
        totalDist = 0
        for group in groups:
            countsInSource = self.countNumsInGroup(group, source)
            countsInTarget = self.countNumsInGroup(group, target)
            totalDist += self.getOccuranceDiff(countsInSource, countsInTarget)
        
        return totalDist
