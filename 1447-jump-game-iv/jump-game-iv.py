class Solution:
    # Again this seems like a grid search
    # We can start by pre-hashing all values = [inds]
    # Then we just include a seen set for inds and also value searches. So O(N + E) like a normal bfs

    def minJumps(self, arr: List[int]) -> int:
        valToInds = {}
        for ind in range(len(arr)):
            val = arr[ind]
            if val in valToInds:
                valToInds[val].append(ind)
            else:    
                valToInds[val] = [ind]
        
        depth = 0
        seenInds = {0}
        seenVals = set()
        exploreQueue = [0]

        while exploreQueue:
            nextQueue = []
            for ind in exploreQueue:
                val = arr[ind]
                if ind == len(arr) - 1:
                    return depth
                
                connections = [ind - 1, ind + 1]
                if val not in seenVals:
                    seenVals.add(val)
                    for conn in valToInds[val]:
                        connections.append(conn)

                for conn in connections:
                    if conn not in seenInds and 0 <= conn < len(arr):
                        nextQueue.append(conn)
                        seenInds.add(conn)

            exploreQueue = nextQueue
            depth += 1

        returb -1