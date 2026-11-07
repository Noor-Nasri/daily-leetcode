class Solution:
    # Seems like straight forward dequeue + priority queue logic
    # While there are servers: We add a task and release any finished server
    # Once we run out of servers; We just look at the server queue, igno
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        solution = [None for i in range(len(tasks))]
        availableServers = [] # (weight, ind)
        reservedServers = [] # (endTime, ind)
        queuedTasks = collections.deque() # taskInd
        for ind in range(len(servers)):
            heappush(availableServers, (servers[ind], ind))

        def processTime(curTime):
            # Handle the existing servers and tasks.
            while reservedServers and reservedServers[0][0] <= curTime:
                _, serverInd = heappop(reservedServers)
                heappush(availableServers, (servers[serverInd], serverInd))
            
            while queuedTasks and availableServers:
                taskInd = queuedTasks.popleft()
                _, serverInd = heappop(availableServers)
                solution[taskInd] = serverInd
                heappush(reservedServers, (curTime + tasks[taskInd], serverInd))

        # Phase 1: Add 1 task per second, and process the queues as we go
        for curTime in range(len(tasks)):
            processTime(curTime)

            if availableServers:
                _, serverInd = heappop(availableServers)
                solution[curTime] = serverInd
                heappush(reservedServers, (curTime + tasks[curTime], serverInd))
            else:
                queuedTasks.append(curTime)
        
        # Phase 2: Now we jump to only the time with fresh servers, and can assign all tasks
        while queuedTasks:
            processTime(reservedServers[0][0])

        return solution
        