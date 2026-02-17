class Solution:
    def recurSearch(self, curInd, numAvailButtons, curNumMins):
        if curInd == 6 and curNumMins >= 60:
            return 
        elif numAvailButtons > len(self.options) - curInd:
            return 
        elif curInd == len(self.options):
            if curNumMins >= 12*60:
                return
            
            numHours = curNumMins // 60
            numMins = int(curNumMins - numHours * 60)
            self.found.add(f"{numHours}:{numMins:02d}")
        else:
            if numAvailButtons:
                self.recurSearch(curInd + 1, numAvailButtons - 1, curNumMins + self.options[curInd])
            self.recurSearch(curInd + 1, numAvailButtons, curNumMins)
            

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.options = [1, 2, 4, 8, 16, 32, 60, 120, 240, 480]
        self.found = set()
        self.recurSearch(0, turnedOn, 0)
        return list(self.found)
        