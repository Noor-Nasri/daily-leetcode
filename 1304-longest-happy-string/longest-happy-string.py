class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a + b + c == 0: return ""
        options_char = ['a', 'b', 'c']
        options_rems = [a, b, c]
        final = []

        while True:
            # put our best option each time (ie one with max vals that is still allowed)
            must_ignore = ''
            if len(final) >= 2 and final[-1] == final[-2]:
                must_ignore = final[-1]

            cur_options = [
                ind for ind in range(3) if options_char[ind] != must_ignore
            ]

            best = sorted(cur_options, key = lambda x : options_rems[x])[-1]
            if not options_rems[best]:
                break # our best choice has 0 remaining occurances
            
            options_rems[best] -= 1
            final.append(options_char[best])

        return "".join(final)