class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        numBeams = 0
        curSecurityDevices = 0
        for row in range(len(bank)):
            nDevices = bank[row].count('1')
            if nDevices:
                numBeams += nDevices*curSecurityDevices
                curSecurityDevices = nDevices
        
        return numBeams