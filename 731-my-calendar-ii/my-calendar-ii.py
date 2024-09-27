class TreeNode:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.doubleBooked = False
        self.start = start
        self.end = end
    
    def hasIntersection(self, start, end):
        if self.end > start and self.start < end: return True
        if end > self.start and start < self.end: return True
        return False

    def verifyAddBooking(self, start, end):
        if not self.hasIntersection(start, end):
            nextNode = (start < self.start) and self.left or self.right
            if nextNode == None: return True
            return nextNode.verifyAddBooking(start, end)

        # intersection, split off bookings
        if self.doubleBooked: return False
        if start < self.start:
            if self.left != None and not self.left.verifyAddBooking(start, self.start): 
                return False
        
        if end > self.end:
            if self.right != None and not self.right.verifyAddBooking(self.end, end): 
                return False

        return True

    def addBooking(self, start, end):
        if not self.hasIntersection(start, end):
            if start < self.start:
                if self.left == None:
                    self.left = TreeNode(start, end)
                else:
                    self.left.addBooking(start, end)
        
            else:
                if self.right == None:
                    self.right = TreeNode(start, end)
                else:
                    self.right.addBooking(start, end)
            return

        # intersection, split off bookings
        self.doubleBooked = True
        startMost = min(self.start, start)
        endMost = max(self.end, end)
        self.start = max(self.start, start)
        self.end = min(self.end, end)

        if startMost < self.start:
            self.addBooking(startMost, self.start)
        
        if endMost > self.end:
            self.addBooking(self.end, endMost)

class MyCalendarTwo:

    def __init__(self):
        self.root = None
    

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        
        if not self.root.verifyAddBooking(start, end):
            return False
        
        self.root.addBooking(start, end)
        return True

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)