# Again this is just a priority queue with update question. Not implemented by default but we can modify heapq

from heapq import heappop, heappush

class TaskManager:
    # Utils
    def addElement(self, userId, taskId, priority):
        entry = [-priority, -taskId, userId]
        self.taskToElement[taskId] = entry
        heappush(self.pq, entry)

    def popElement(self, taskId):
        entry = self.taskToElement.pop(taskId)
        userId = entry[2]
        entry[2] = -1
        return userId

    def changePriority(self, taskId, newPriority):
        _, _, userId = self.taskToElement[taskId]
        self.popElement(taskId)
        self.addElement(userId, taskId, newPriority)

    def popTop(self):
        while self.pq and self.pq[0][2] == -1:
            heappop(self.pq)
    
        if not self.pq:
            return -1
        
        return self.popElement(-self.pq[0][1])

    # Base
    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.taskToElement = {}
        for userId, taskId, priority in tasks:
            self.addElement(userId, taskId, priority)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.addElement(userId, taskId, priority)
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.changePriority(taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        self.popElement(taskId)
        

    def execTop(self) -> int:
        return self.popTop()
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()