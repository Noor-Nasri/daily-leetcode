class TreeNode:
    def __init__(self, start, end, numCount = 1):
        self.left = None
        self.right = None
        self.numBookings = numCount
        self.start = start
        self.end = end
    
    def hasIntersection(self, start, end):
        return self.end > start and self.start < end


    def addBooking(self, start, end, numCount = 1):
        # adds booking, returns max number of extra bookings involving it
        if not self.hasIntersection(start, end):
            if start < self.start:
                if self.left == None:
                    self.left = TreeNode(start, end, numCount)
                    return 1
                else:
                    return self.left.addBooking(start, end, numCount)
        
            else:
                if self.right == None:
                    self.right = TreeNode(start, end, numCount)
                    return 1
                else:
                    return self.right.addBooking(start, end, numCount)

        # intersection, split off bookings
        maxFound = 1
        if start < self.start:
            # add numCount on the left
            maxFound = max(maxFound, self.addBooking(start, self.start, numCount))
        
        if end > self.end:
            # add numCount on the right
            maxFound = max(maxFound, self.addBooking(self.end, end, numCount))


        if self.start < start:
            # will need to split off our event to add this conflict 
            prevStart = self.start
            self.start = start
            self.addBooking(prevStart, start, self.numBookings)

        if self.end > end:
            # will need to split off our event to add this conflict 
            prevEnd = self.end
            self.end = end
            self.addBooking(end, prevEnd, self.numBookings)

        self.numBookings += numCount
        return max(self.numBookings, maxFound)


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
class MyCalendarThree:
    def __init__(self):
        self.root = None
        self.max = 1
        

    def book(self, startTime: int, endTime: int) -> int:
        if not self.root:
            self.root = TreeNode(startTime, endTime)
            return 1
        
        self.max = max(self.max, self.root.addBooking(startTime, endTime))
        return self.max
        

