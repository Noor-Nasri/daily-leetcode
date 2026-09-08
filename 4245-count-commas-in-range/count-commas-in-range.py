class Solution:
    # This is too easy to even do a loop
    # Every number between 1,000 and the limit of 100,000 has one comma
    def countCommas(self, n: int) -> int:
        return max(0, n - 999)
        