class Solution:
    # I mean this can be brute forced but whats the fun in that
    # The real question is: when is it ever impossible?
    # If you have odd, even -> turn even into odd by subtracting odd
    # If you have odd, odd or even, even -> keep as is.
    # So its always true?? lol lets try

    def uniformArray(self, nums1: list[int]) -> bool:
        return True