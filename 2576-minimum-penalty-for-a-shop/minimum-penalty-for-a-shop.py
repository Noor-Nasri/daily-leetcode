class Solution:
    def bestClosingTime(self, customers: str) -> int:
        numCust = [c == "Y" and 1 or 0 for c in customers]
        numEmptyBeforeInd = [0 for i in range(len(customers) + 1)]
        for ind in range(1, len(customers) + 1):
            numEmptyBeforeInd[ind] = numEmptyBeforeInd[ind - 1] + (1 - numCust[ind - 1])

        numCustFromInd = [0 for i in range(len(customers) + 1)]
        for ind in range(len(customers) - 1, -1, -1):
            c = customers[ind]
            numCustFromInd[ind] = numCustFromInd[ind + 1] + numCust[ind]
        
        earliestHour = -1
        leastPenalty = float('inf')
        for hour in range(len(customers) + 1):
            penalty = numEmptyBeforeInd[hour] + numCustFromInd[hour]
            if penalty < leastPenalty:
                leastPenalty = penalty
                earliestHour = hour
        
        return earliestHour

