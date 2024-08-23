
class Solution:
    def gcdHelper(self, num, denom):
        gcd = math.gcd(num, denom)
        num //= gcd
        denom //= gcd
        return (num, denom)


    def fractionAddition(self, expression: str) -> str:
        total_num = 0
        total_denom = 1

        expression = expression.replace("-", "+-")

        for term in expression.split("+"):
            if not term: continue
            numerator, denom = [int(e) for e in term.split("/")]
            
            if total_denom % denom == 0:
                total_num += numerator * (total_denom // denom )
            elif denom % total_denom == 0:
                total_num *= (denom // total_denom)
                total_denom = denom
                total_num += numerator
            else:
                total_num *= denom
                numerator *= total_denom
                total_num += numerator
                total_denom *= denom
            
            total_num, total_denom = self.gcdHelper(total_num, total_denom)
        
        return f"{total_num}/{total_denom}"



