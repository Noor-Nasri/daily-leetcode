class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counts = {}
        for move in moves:
            counts[move] = counts.get(move, 0) + 1
        
        return counts.get("U", 0) == counts.get("D", 0) and counts.get("L", 0) == counts.get("R", 0)
        