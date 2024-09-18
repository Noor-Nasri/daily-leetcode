import functools

def compare(a, b):
        num1 = int(a + b)
        num2 = int(b + a)
        if num1 > num2:
            return -1
        elif num1 < num2:
            return 1
        return 0
class Solution:
    
    '''
    # full number will always have same number of digits
    # therefore just put bigger digits first
    # if [34] vs [344], take 344 cuz 4 is better than our current best first digit (3)
    # if [34] vs [343], take 34 cuz it won't make a diff
    for dig_ind in range(min(len(a), len(b))):
        dig1 = int(a[dig_ind])
        dig2 = int(b[dig_ind])

        if dig1 == dig2:
            continue

        if dig1 > dig2: # a is bigger, should be considered first
            return -1
        else: # b is bigger, should be taken first
            return 1
    
    if len(a) == len(b): return 0
    
    firstDig = int(a[0])
    if len(a) < len(b):
        nextDig = int(b[len(a)])
        if nextDig > firstDig:

    
    else:
        # when right element is bigger than starter, take it first
        nextDig = int(a[len(b)])
        return nextDig > firstDig
    '''
        
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"
            
        vals = [str(e) for e in nums]
        vals = sorted(vals, key = functools.cmp_to_key(compare))
        return "".join(vals)
        