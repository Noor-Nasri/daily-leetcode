class Solution:
    def isValidCode(self, code, allowedChars):
        if not code:
            return False

        for c in code:
            if c not in allowedChars:
                return False
                
        return True

        
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        allowedChars = ["_"]
        for i in range(26):
            allowedChars.append(chr(ord('a') + i))
            allowedChars.append(chr(ord('A') + i))
        for i in range(10):
            allowedChars.append(str(i))
        allowedChars = set(allowedChars)

        buckets = {
            "electronics": [],
            "grocery": [],
            "pharmacy": [],
            "restaurant": []
        }

        for ind in range(len(code)):
            if isActive[ind] and businessLine[ind] in buckets and self.isValidCode(code[ind], allowedChars):
                buckets[businessLine[ind]].append(code[ind])


        result = []
        for bucket in buckets:
            codes = sorted(buckets[bucket])
            result += codes

        return result
                
        