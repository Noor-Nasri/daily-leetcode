# I am just submitting a one liner for this to test the 'time travel' feature in leetcode
class Solution:
    def singleNumber(self, a: List[int]) -> List[int]:
        return (x:=reduce(xor,a))^(y:=reduce(xor,(v for v in a if -x&x&v))),y