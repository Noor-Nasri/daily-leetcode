class Solution:
    # This comes down to finding the connected components then answering component[u] == component[v]
    # The tricky part is resolving the components without n^2. Technically there can be n^2 edges.
    # Okay, actually there is a simple trick here: just sort and look for gaps > maxDiff!
    # Since vals <= maxDiff apart are connected, then we keep chaining the inds until the gap is too big


    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        numIndPairs = sorted([(nums[i], i) for i in range(n)])
        componentIds = [-1 for i in range(n)]
        curComponentId = -1
        lastVal = -maxDiff-1

        for val, ind in numIndPairs:
            if val > lastVal + maxDiff:
                curComponentId += 1
            
            componentIds[ind] = curComponentId
            lastVal = val
        
        results = []
        for a, b in queries:
            results.append(componentIds[a] == componentIds[b])

        return results
