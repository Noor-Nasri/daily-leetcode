class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dists = [i for i in range(n)]
        children = [[i + 1] for i in range(n - 1)]
        results = []

        def checkIfImproved(node, possibleDist):
            if possibleDist >= dists[node]: return
            dists[node] = possibleDist
            if node == n - 1: return
            
            # I cant think of a decent way .. this is just limited to n^2 total
            for child in children[node]:
                checkIfImproved(child, possibleDist + 1)

        for u, v in queries:
            children[u].append(v)
            checkIfImproved(v, dists[u] + 1)
            results.append(dists[-1])

        return results
        