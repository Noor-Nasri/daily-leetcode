class MyCalendar:

    def __init__(self):
        self.times = []    
    
    def book(self, start: int, end: int) -> bool:
        for s, e in self.times:
            # case 1: new event captures this s,e
            if start < e and end > s:
                return False
            
            # case 2: new event is inside old event
            if s < end and e > start:
                return False
        
        self.times.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)