class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = str(bin(start))[2:]
        goal = str(bin(goal))[2:]
        l = max(len(start), len(goal))

        if len(start) < l: start = "0"*(l - len(start)) + start
        if len(goal) < l: goal = "0"*(l - len(goal)) + goal

        diff = sum(int(start[i] != goal[i])  for i in range(l))
        return diff
        