from collections import deque

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # some sort of greedy to determine the shortest beutiful string
        # If multiple of same length as shortest, store in list and later get best

        best_solutions = []
        solution_len = 101 # Max is 101

        cur_ones = deque()
        for ind in range(len(s)):
            if s[ind] != '1': continue

            if len(cur_ones) < k:
                cur_ones.append(ind)
            else:
                cur_ones.popleft()
                cur_ones.append(ind)
            
            if len(cur_ones) == k:
                length_cur = cur_ones[len(cur_ones) - 1] - cur_ones[0] + 1
                if length_cur == solution_len:
                    best_solutions.append((cur_ones[0], cur_ones[len(cur_ones) - 1]))
                elif length_cur < solution_len:
                    solution_len = length_cur
                    best_solutions = [(cur_ones[0], cur_ones[len(cur_ones) - 1])]
        
        if not best_solutions: return ""
        strings = [s[start:end+1] for start, end in best_solutions]
        return min(strings)
