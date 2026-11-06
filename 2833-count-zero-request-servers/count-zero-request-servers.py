class Solution:
    # Too many moving parts. Lets say we process logs and queries in order.
    # Going through all the logs, we maintain the # of sleeping servers
    # When we get an event, we consider the server taken until time+x. Then we free it.
    # Okay, I think this is basic implementation by iterating on the 10^6 time units
    # for funsies, we will do the proper priority queue setup and look at everything in order

    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        queries = sorted([(queries[ind], ind) for ind in range(len(queries))])
        results = [0 for i in range(len(queries))]
        pingQueue = [e[::-1] for e in logs]
        heapify(pingQueue) # we can do sorted lists but I'd rather queues..
        sleepQueue = []

        countAsleep = n
        serverSleepTime = {} # Track latest time for server to sleep, in case of multiple logs
        
        for queryTime, queryInd in queries:
            # Before we run this query, start by activating all servers with logs <= time
            while pingQueue and pingQueue[0][0] <= queryTime:
                pingTime, serverId = heappop(pingQueue)
                if serverId not in serverSleepTime:
                    countAsleep -= 1

                serverSleepTime[serverId] = pingTime + x
                heappush(sleepQueue, (pingTime + x, serverId))

            # Now remove any servers that finished their pings
            while sleepQueue and sleepQueue[0][0] < queryTime:
                _, serverId = heappop(sleepQueue)
                if serverId in serverSleepTime and serverSleepTime[serverId] < queryTime:
                    countAsleep += 1
                    del serverSleepTime[serverId]
            
            results[queryInd] = countAsleep
        
        return results


