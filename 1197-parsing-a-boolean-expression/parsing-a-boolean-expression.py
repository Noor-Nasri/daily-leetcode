class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        # I am moving places so this is a temp solution to keep the daily streak
        return all(len(s:=re.sub(r'([&|!])\([tf,]+\)',lambda m:'tft'[m[1]=='|':]['tf'[m[1]=='&'] in m[0]],s))>1 for _ in s) or s>'f'