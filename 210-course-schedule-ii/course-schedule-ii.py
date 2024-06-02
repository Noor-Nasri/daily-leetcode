class Solution:
    
    def addCourse(self, course: int, inCall: dict) -> bool: # false if impossible
        if course in self.alreadyInserted: return True
        
        inCall[course] = True
        for preReq in self.mapping[course]:
            if preReq in inCall and inCall[preReq]: return False
            
            inCall[preReq] = True
            if not self.addCourse(preReq, inCall): return False
            inCall[preReq] = False
        
        self.finalList.append(course)
        self.alreadyInserted[course] = True
        return True
        
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.mapping = [[] for i in range(numCourses)]
        
        for preReqPair in prerequisites:
            wanted,prequisite = preReqPair
            self.mapping[wanted].append(prequisite)
            
        self.finalList = []
        self.alreadyInserted = {}
        
        for course in range(numCourses):
            if not self.addCourse(course, {}):
                return []
            
        return self.finalList
            
        