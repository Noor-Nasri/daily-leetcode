from heapq import heappop, heappush

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Suppose you are at ind 0, then you need to accept X initial queries. Just pick the ones that extend the most
        # Then as you proceed, keep considering only the ones that end last to give you the most help
        queries = sorted(queries)
        ind_n = 0
        ind_q = 0
        queriesUsed = 0
        availableQueries = []
        activeQueries = []

        while ind_n < len(nums):
            #print("LOOKING AT IND", ind_n)
            # Move through the numbers one at a time
            # Step 1: Start considering all queries that now start
            while ind_q < len(queries) and queries[ind_q][0] == ind_n:
                heappush(availableQueries, -queries[ind_q][1])
                ind_q += 1
            
            #print("Available queries: ", availableQueries)

            # Step 2: Forget about queries that stopped applying to us
            while activeQueries and activeQueries[0] < ind_n:
                heappop(activeQueries)
            
            #print("Active queries: ", activeQueries)

            # Step 3: Take as many new queries as needed, greedily taking last one
            while availableQueries and len(activeQueries) < nums[ind_n] and -availableQueries[0] >= ind_n:
                bestQuery = -heappop(availableQueries)
                heappush(activeQueries, bestQuery)
                queriesUsed += 1
                #print("Added top query", bestQuery)
            
            # Step 4: Verify valid
            if len(activeQueries) < nums[ind_n]:
                #print("Impossible:", len(activeQueries), nums[ind_n])
                return -1

            ind_n += 1



        return len(queries) -  queriesUsed
        
        