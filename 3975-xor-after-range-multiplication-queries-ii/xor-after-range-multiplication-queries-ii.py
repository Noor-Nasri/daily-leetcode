class Solution:
    # Running the queries is not possible, since thats n^2.
    # If we go one ind at a time, then even if we know all relevant queries it will be n^2 to check them
    # For XOR: each digit is based on the # of inds that have a 1 in that digit, after all operations

    # This is hard. Maybe we can sweep through indices, then pick up new queries as we go
    # We would need to somehow only acknowledge the query once, instead of every k indices. 
    # Can we group queries based on start and skip? Okay, then what ..

    # If we group queries by where they start and jump, we can reduce each group to a final multiplier.
    # Then we can push the entire group to next ind each time. Will this still TLE?
    # For queries with k >= 1000, each query is only going to be relevant 100 times max so we can ignore it (10^7).
    # How many groups of k <= 1000 exist? You can have 2 groups of k=2, 3 groups of k=3, etc. So 1000^2.
    # BUT - at any given numInd, only one group per k-value can exist! So max 1000 iterations at a given ind.
    # So we have at most 10^8 iterations! It could work .. but we may need to optimize 

    # It did not work :(. I think maintaining this active set is too expensive. Maybe I just solve >= 500 first,
    # Then for steps <= 500 I have a very primative loop that multiplies all groups that *should* be active
    # Ie, this is 500*n but we don't have to maintain sets and re-pushing groups to next ind.
    # At each numInd, we try step=1, 500. Then we get groupProd[step][numInd % step] 

    # Still TLE .. I will reorganize the small queries to solve one group at a time, to avoid maintaining active groups

    def simulateLargeQueries(self, nums, queries, CUTOFF):
        MOD = 10**9 + 7
        remainingQueries = []
        maxStep = 0
        for queryInd in range(len(queries)):
            start, end, step, mult = queries[queryInd]
            if step < CUTOFF:
                maxStep = max(maxStep, step)
                remainingQueries.append(queries[queryInd])
                continue

            for numInd in range(start, end + 1, step):
                nums[numInd] = (nums[numInd] * mult) % MOD
        
        return maxStep, remainingQueries

    def groupSmallQueries(self, queries, maxStep):
        queryIndsFromStartFromStep = {}
        for queryInd in range(len(queries)):
            start, end, step, mult = queries[queryInd]
            if step not in queryIndsFromStartFromStep:
                queryIndsFromStartFromStep[step] = {}

            realStart = start % step
            if realStart not in queryIndsFromStartFromStep[step]:
                queryIndsFromStartFromStep[step][realStart] = []

            queryIndsFromStartFromStep[step][realStart].append(queryInd)

        return queryIndsFromStartFromStep
    
    def applyGroup(self, nums, queries, groupedQueryList, firstNumInd, step):
        # This method is called up to 5000 times, with average inner loop of 2000 iters
        # We must be fully optimal to avoid TLE here.
        MOD = 10**9 + 7
        curProd = 1
        prodRemovals = [] # (final ind, mult)
        groupedQueryInd = 0

        for numInd in range(firstNumInd, len(nums), step):
            # First apply all new queries to active product, then remove finished ones
            while groupedQueryInd < len(groupedQueryList) and queries[groupedQueryList[groupedQueryInd]][0] == numInd:
                _, end, _, mult = queries[groupedQueryList[groupedQueryInd]]
                curProd = (curProd * mult) % MOD
                heappush(prodRemovals, (end, mult))
                groupedQueryInd += 1
            
            while prodRemovals and prodRemovals[0][0] < numInd:
                _, deadMult = heappop(prodRemovals)
                modInverse = pow(deadMult, MOD-2, MOD)
                curProd = (curProd * modInverse) % MOD
            
            nums[numInd] = (nums[numInd] * curProd) % MOD


    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        CUTOFF = 100 # This makes it an even split: large queries each cost 10^3, so we can afford them all
        MOD = 10**9 + 7
        maxStep, queries = self.simulateLargeQueries(nums, queries, CUTOFF)
        queries = sorted(queries)
        queryIndsFromStartFromStep = self.groupSmallQueries(queries, maxStep)
        
        for step in queryIndsFromStartFromStep:
            for firstInd in queryIndsFromStartFromStep[step]:
                groupedQueryList = queryIndsFromStartFromStep[step][firstInd]
                self.applyGroup(nums, queries, groupedQueryList, firstInd, step)

        finalXor = 0
        for num in nums:
            finalXor ^= num
        return finalXor