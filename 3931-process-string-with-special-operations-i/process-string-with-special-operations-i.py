class Solution:
    # So * makes it seem like a stack question, but that means 2x at each #
    # BUT - since each item we add would be in the final answer anyways, its all the same
    # .. so we're supposed to just brute force it through stack since s <= 20..
    
    # I think the elegant solution is to build the stack then recreate backwards
    # Ie the # means everything solve the rest, then put the answer twice.
    # But no matter what, the complexity will be O(2^s) because the solution can be that long

    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c == "*":
                if result:
                    result.pop()
            elif c == "#":
                for i in range(len(result)):
                    result.append(result[i])
            elif c == "%":
                result = result[::-1]
            else:
                result.append(c)
        
        return "".join(result)