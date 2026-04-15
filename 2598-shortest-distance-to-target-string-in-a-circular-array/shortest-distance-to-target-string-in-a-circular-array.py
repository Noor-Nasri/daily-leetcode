class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        for offset in range(len(words) // 2 + 1):
            if words[(startIndex - offset) % len(words)] == target or words[(startIndex + offset) % len(words)] == target:
                return offset
        
        return -1