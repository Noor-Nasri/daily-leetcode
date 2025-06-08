class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # 1 .. 10 .. 100
        # then go up til desired. And when hitting a few degit: eg 200, we first want the shorter types
        # 2, 20, etc.
        # Too much of a hassle 
        return [int(e) for e in sorted([str(i) for i in range(1, n+1)])]
        