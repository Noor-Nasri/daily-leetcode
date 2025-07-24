class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)

        for batch_start_ind in range(0, len(s), 2 * k):
            i = batch_start_ind
            j = min(i + k, len(s)) - 1
            
            while i <= j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)

