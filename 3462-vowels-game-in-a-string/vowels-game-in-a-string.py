class Solution:
    # The whole substring thing doesn't matter. There are x vowels, and Alice can remove an odd number while bob an even
    # So, if x = 6, Alice can take 5 and end the game. If x = 7, Alice can take 7 and end the game..
    # So just, Alice wins as long as there are vowels??? Lol
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for c in s:
            if c in vowels:
                count += 1
        return count >= 1
        