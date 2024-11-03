class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_expected = (len(rolls) + n) * mean
        total_missing = total_expected - sum(rolls)
        if total_missing < n: return [] 
        if total_missing > n*6: return []

        result = [1 for i in range(n)]
        total_made = n
        ind = 0
        while total_made != total_missing:
            newVal = min(6, total_missing - total_made + 1)
            total_made += newVal - 1
            result[ind] = newVal
            ind += 1

        return result

        