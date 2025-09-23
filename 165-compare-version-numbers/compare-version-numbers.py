class Solution:
    def compareLists(self, L1, L2, ind):
        if ind >= len(L1) and ind >= len(L2):
            return 0

        v1 = ind < len(L1) and L1[ind] or 0
        v2 = ind < len(L2) and L2[ind] or 0
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        
        return self.compareLists(L1, L2, ind + 1)
        
    def compareVersion(self, version1: str, version2: str) -> int:
        L1 = [int(e) for e in version1.split('.')]
        L2 = [int(e) for e in version2.split('.')]
        return self.compareLists(L1, L2, 0)
        
        