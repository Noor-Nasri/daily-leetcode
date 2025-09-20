from collections import deque

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.orderedPackets = deque()
        self.destToTimes = {}
        self.currentPackets = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        newPacket = (source, destination, timestamp)
        if newPacket in self.currentPackets:
            return False

        if len(self.orderedPackets) == self.memoryLimit:
            oldS, oldD, oldT = self.orderedPackets.popleft()
            self.destToTimes[oldD].popleft()
            self.currentPackets.remove((oldS, oldD, oldT))

        self.orderedPackets.append(newPacket)
        if destination not in self.destToTimes:
            self.destToTimes[destination] = deque()
            
        self.destToTimes[destination].append(timestamp)
        self.currentPackets.add(newPacket)
        return True
            

    def forwardPacket(self) -> List[int]:
        if len(self.orderedPackets) == 0:
            return []
            
        oldS, oldD, oldT = self.orderedPackets.popleft()
        self.destToTimes[oldD].popleft()
        self.currentPackets.remove((oldS, oldD, oldT))
        return [oldS, oldD, oldT]
        

    def binarySearchForIndexLeft(self, times, target):
        # index of target if it was to be inserted into sorted list, placed BEFORE dupes
        if target <= times[0]:
            return 0
        if target > times[-1]:
            return len(times)

        best = None
        low = 1
        high = len(times) - 1

        while low <= high:
            mid = (low + high) // 2
            if times[mid] >= target:
                best = mid
                high = mid - 1
            else:
                low = mid + 1

        return best

    def binarySearchForIndexRight(self, times, target):
        # index of target if it was to be inserted into sorted list, placed AFTER dupes
        if target < times[0]:
            return 0
        if target >= times[-1]:
            return len(times)

        best = None
        low = 0
        high = len(times) - 2

        while low <= high:
            mid = (low + high) // 2
            if times[mid] <= target:
                best = mid
                low = mid + 1
            else:
                high = mid - 1

        return best + 1
        
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destToTimes or len(self.destToTimes[destination]) == 0:
            return 0
            
        indST = self.binarySearchForIndexLeft(self.destToTimes[destination], startTime)
        indED = self.binarySearchForIndexRight(self.destToTimes[destination], endTime)
        #print(self.destToTimes[destination])
        #print(indST, indED)
        return indED - indST
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)