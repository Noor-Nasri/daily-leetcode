class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        items = [ (names[i], heights[i]) for i in range(len(names))]
        items = sorted(items, key = lambda x : -x[1])

        return [item[0] for item in items]
        