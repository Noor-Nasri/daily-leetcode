class Solution:
    # So this is a basic implementation question that gets complicated due to strings
    # Actually since we are told its not nested, we can indeed just use strings.
    # Just scan inds for open and closed, then go back a second time and add everything. O(n)
    # I was gonna do a rolling hash, no need ig

    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = {e[0] : e[1] for e in knowledge}
        #print(mapping)
        finalString = []
        isInBrackets = False
        curBracketString = []

        for c in s:
            if c == "(":
                isInBrackets = True
            elif c == ")":
                key = "".join(curBracketString)
                #print("Searching for", key)
                finalString.append(mapping.get(key, "?"))
                isInBrackets = False
                curBracketString = []
            elif isInBrackets:
                curBracketString.append(c)
            else:
                finalString.append(c)
        
            #print(finalString)
        return "".join(finalString)
