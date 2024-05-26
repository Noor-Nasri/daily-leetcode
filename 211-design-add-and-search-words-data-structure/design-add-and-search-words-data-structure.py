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

    def getMatches(self, word: str, curInd: int, curDict):
        char = word[curInd]
        matches = []
        if char == ".":
            for key in curDict:
                if key == "FINAL": continue
                matches.append(curDict[key])
        else:
            if char in curDict:
                matches.append(curDict[char])
            if "." in curDict:
                matches.append(curDict["."])
        
        return matches

    
    def search(self, word: str) -> bool:
        #print("SEARCHING FOR:", word)
        matches = self.getMatches(word, 0, self.initDict)
        curInd = 0

        while matches:
            #print(curInd, matches)

            curInd += 1
            if curInd == len(word):
                # see if any matches are done
                for match in matches:
                    if 'FINAL' in match: return True
                return False
            
            nextMatches = []
            for curDict in matches:
                nextMatches += self.getMatches(word, curInd, curDict)

            matches = nextMatches
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)