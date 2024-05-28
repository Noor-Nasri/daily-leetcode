class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        # DP Recur is simply: each char can come from s1 or s2
        solutions = {}
        def recur(ind1, ind2, ind3):
            if ind3 == len(s3): return True

            if (ind1, ind2, ind3) in solutions:
                return solutions[(ind1, ind2, ind3)]
            
            option1 = False
            if (ind1 < len(s1)) and s1[ind1] == s3[ind3]:
                option1 = recur(ind1 + 1, ind2, ind3 + 1)
            
            option2 = False
            if (ind2 < len(s2)) and s2[ind2] == s3[ind3]:
                option2 = recur(ind1, ind2 + 1, ind3 + 1)
            
            sol = option1 or option2
            solutions[(ind1, ind2, ind3)] = sol
            return sol
        
        return recur(0, 0, 0)

            
        