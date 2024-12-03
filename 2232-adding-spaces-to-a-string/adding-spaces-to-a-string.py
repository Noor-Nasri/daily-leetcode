class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        letters = list(s)
        final = []
        for ind in range(len(letters) - 1, -1, -1):
            final.append(letters.pop())
            if spaces and spaces[-1] == ind:
                final.append(' ')
                spaces.pop()

        return "".join(final[::-1])
        