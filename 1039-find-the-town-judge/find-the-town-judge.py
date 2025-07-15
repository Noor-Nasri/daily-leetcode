class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        conns = [set() for i in range(n)]
        for u, v in trust:
            conns[u-1].add(v-1)
        
        judgeInd = -1
        for person in range(n):
            if len(conns[person]) == 0:
                if judgeInd != -1:
                    return -1
                
                judgeInd = person
        
        for person in range(n):
            if person != judgeInd and judgeInd not in conns[person]:
                return -1
        
        return judgeInd + 1