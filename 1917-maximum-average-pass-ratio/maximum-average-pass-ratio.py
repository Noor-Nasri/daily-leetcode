from heapq import heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        data = []
        for npass, ntot in classes:
            increase = (npass + 1) / (ntot + 1)  - npass / ntot 
            heappush(data, (-increase, npass, ntot))
        
        for i in range(extraStudents):
            _, npass, ntot = heappop(data)
            npass += 1
            ntot += 1
            increase = (npass + 1) / (ntot + 1)  - npass / ntot 
            heappush(data, (-increase, npass, ntot))

        tot = sum(e[1]/e[2] for e in data)
        return tot/len(classes)
        