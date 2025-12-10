from math import factorial
class Solution:
    # Once you take complexity x, you can take future inds with vals >= x in any order
    # So at a given ind: if you take it, you can take all those other vals out and simply multiply the possible combos

    # Okay wait. If any val <= starting complexity, the question is unsolvable.
    # And if all vals >  starting complexity, they can all just be taken in any order.
    # Lol, this is just factorial.

    def countPermutations(self, complexity: List[int]) -> int:
        if len(complexity) == 1:
            return 1

        lowest = min(complexity[1:])
        if lowest <= complexity[0]:
            return 0
        
        return factorial(len(complexity) - 1) % (10**9 + 7)