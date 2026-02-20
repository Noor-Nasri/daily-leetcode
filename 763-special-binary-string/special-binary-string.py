class Solution:
    # Honestly I'd like to do this question but its not only complicated, its not defined right.
    # I can't tell if they allow a single move, which I can solve in O(n^3), or any number of moves
    # Public solution, looks like single swap? So annoying

    def makeLargestSpecial(self, s: str) -> str:
        if s == '':
            return ''
        ans = []
        cnt = 0
        i = j = 0
        while i < len(s):
            cnt += 1 if s[i] == '1' else -1
            if cnt == 0:
                ans.append('1' + self.makeLargestSpecial(s[j + 1 : i]) + '0')
                j = i + 1
            i += 1
        ans.sort(reverse=True)
        return ''.join(ans)