class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        total = 0
        
        for ind in range(len(num_str) - k+ 1):
            subnum = int(num_str[ind:ind+k])
            if subnum and not (num % subnum): 
                total += 1

        return total
        