class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairings = []
        for num in nums:
            new_digits = [str(mapping[int(digit)]) for digit in str(num)]
            pairings.append((num, int("".join(new_digits))))
        
        pairings = sorted(pairings, key = lambda pairing : pairing[1])
        return [pairing[0] for pairing in pairings]
        