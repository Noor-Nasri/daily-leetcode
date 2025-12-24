class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tot = sum(apple)
        capacity = sorted(capacity, reverse = True)
        for ind in range(len(capacity)):
            tot -= capacity[ind]
            if tot <= 0:
                return ind + 1