class Solution:
    def prereqSolver(self, prereqs, canTake, tryingToTake, course):
        if not prereqs[course]:
            canTake.add(course)
            return True
        
        tryingToTake.add(course)
        success = True
        for pre in prereqs[course]:
            if pre in tryingToTake: return False
            if pre in canTake: continue

            success = self.prereqSolver(prereqs, canTake, tryingToTake, pre)
            if not success: return False
        
        tryingToTake.remove(course)
        canTake.add(course)
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[] for j in range(numCourses)]
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        canTake = set()
        tryingToTake = set()
        for course in range(numCourses):
            if course in canTake: continue
            if not self.prereqSolver(prereqs, canTake, tryingToTake, course):
                return False
        
        return True
            
        