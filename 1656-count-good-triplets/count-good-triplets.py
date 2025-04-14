class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        numFound = 0
        for ind1 in range(len(arr)):
            for ind2 in range(ind1 + 1, len(arr)):
                if abs(arr[ind2] - arr[ind1]) > a:
                    continue

                for ind3 in range(ind2 + 1, len(arr)):
                    if abs(arr[ind2] - arr[ind3]) <= b and abs(arr[ind1] - arr[ind3]) <= c:
                        numFound += 1
        
        return numFound


        