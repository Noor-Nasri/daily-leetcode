class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(e[11:13])>60 for e in details)

        