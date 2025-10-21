class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(["++" in e and 1 or -1 for e in operations])
        