class WordDictionary:
    # After implementing, I realized people used trees for this
    # Instead, I figured the best approach is nested hash maps
    # While this is a bit more unique, I still think it is a better fit
    # based on the problem discription. 
    # add runs in O(word.length) = O(1), and search acts as a short graph

    def __init__(self):
        self.initDict = {}
        
    def recurLetter(self, word: str, curInd: int, curDict):
        if len(word) == curInd:
            curDict['FINAL'] = True
            return
        
        char = word[curInd]
        if not (char in curDict):
            curDict[char] = {}
        
        self.recurLetter(word, curInd + 1, curDict[char])

    def addWord(self, word: str) -> None:
        self.recurLetter(word, 0, self.initDict)

    
    def search(self, word: str) -> bool:
        #print("SEARCHING FOR:", word)
        matches = [self.initDict]
        curInd = -1

        while True:
            #print(curInd, matches)

            curInd += 1
            if curInd == len(word):
                # see if any matches are done
                for match in matches:
                    if 'FINAL' in match: return True
                return False
            
            char = word[curInd]
            nextMatches = []
            for curDict in matches:
                if char == ".":
                    for key in curDict:
                        if key == "FINAL": continue
                        nextMatches.append(curDict[key])
                else:
                    if char in curDict:
                        nextMatches.append(curDict[char])
                    if "." in curDict:
                        nextMatches.append(curDict["."])
        
            matches = nextMatches

            if not matches:
                break
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)