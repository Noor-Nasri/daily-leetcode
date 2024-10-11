from random import shuffle

class TreeNode:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
    
    def addNode(self, start, end):
        if start < self.start:
            if self.left == None:
                self.left = TreeNode(start, end)
            else:
                self.left.addNode(start, end)
        else:
            if self.right == None:
                self.right = TreeNode(start, end)
            else:
                self.right.addNode(start, end)
    
    def getZucc(self):
        if self.left.left == None:
            # successor is self.left
            zucc = self.left
            self.left = self.left.right
            return zucc

        return self.left.getZucc()


    def suicide(self):
        # return replacement
        if self.left == None and self.right == None:
            return None

        elif self.left == None:
            return self.right

        elif self.right == None:
            return self.left
        
        # two children, do succ
        if self.right.left == None:
            self.right.left = self.left
            return self.right

        zucc = self.right.getZucc() # cant be self.right ..
        zucc.left = self.left
        zucc.right = self.right
        return zucc
            

    def popEarliestAfterTime(self, start):
        if self.start < start:
            # need bigger elements
            if self.right == None:
                return (self, None, None)
            
            r, s, e = self.right.popEarliestAfterTime(start)
            self.right = r
            return (self, s, e)

        # this node is valid, see if there is more optimal to the left
        if self.left != None:
            l, s, e = self.left.popEarliestAfterTime(start)
            if s != None:
                self.left = l
                return (self, s, e)

        # this is the earliest node >= start
        replacement = self.suicide()
        return (replacement, self.start, self.end)


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # idea is simple: seat 0 is always prefered. So earliest guy takes it
        # the moment seat 0 becomes available, next guy to show up takes it
        # so just figure out who sits on seat 0s, then seat 1s, etc, until we reach our guy
        
        desired_guy_start = times[targetFriend][0]

        times_bystart = sorted(times, key = lambda x: x[0], reverse = True)
        root = TreeNode(times[0][0], times[0][1])
        insertion_order = [i for i in range(1, len(times))]
        shuffle(insertion_order)
        for ind in insertion_order:
            root.addNode(times[ind][0], times[ind][1])
        self.assigned = set()

        for chair in range(len(times)):
            # worst case, our friend sits at chair n-1
            while times_bystart[-1][0] in self.assigned:
                times_bystart.pop()
            
            start_time = times_bystart[-1][0]
            while True:
                root, s, e = root.popEarliestAfterTime(start_time)
                
                if s == desired_guy_start:
                    return chair

                if s == None: 
                    break
                
                self.assigned.add(s) 
                start_time = e
        
        assert("Yo mama" == "skinny")
        