class Solution:
    def bestClosingTime(self, customers: str) -> int:
        numEmptyBeforeInd = [0 for i in range(len(customers) + 1)]
        for ind in range(1, len(customers) + 1):
            c = customers[ind - 1]
            numEmptyBeforeInd[ind] = numEmptyBeforeInd[ind - 1] + int(c == "N")

        numCustFromInd = [0 for i in range(len(customers) + 1)]
        for ind in range(len(customers) - 1, -1, -1):
            c = customers[ind]
            numCustFromInd[ind] = numCustFromInd[ind + 1] + int(c == "Y")
        
        earliestHour = -1
        leastPenalty = float('inf')
        for hour in range(len(customers) + 1):
            penalty = numEmptyBeforeInd[hour] + numCustFromInd[hour]
            if penalty < leastPenalty:
                leastPenalty = penalty
                earliestHour = hour
        
        return earliestHour

