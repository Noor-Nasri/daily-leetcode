# Catching capitalization is simple hashmap, but what about vowels?
# If we have a trie structure, we could trace all options then take highest priority ..

vowels = {'a', 'e', 'i', 'o', 'u'}
vowelBucketInds = {ord(e) - 97 for e in vowels}
class TrieNode:
    def __init__(self):
        self.buckets = [None for i in range(26)]
        self.wordInd = 5001
    
    def addWord(self, wordlist, wordInd, letterInd):
        word = wordlist[wordInd]
        if letterInd == len(word):
            self.wordInd = min(self.wordInd, wordInd)
            return

        bucket = ord(word[letterInd].lower()) - 97
        if self.buckets[bucket] == None:
            self.buckets[bucket] = TrieNode()
        
        self.buckets[bucket].addWord(wordlist, wordInd, letterInd + 1)

    def getBestMatch(self, query, queryInd):
        if queryInd == len(query):
            return self.wordInd
        
        bucket = ord(query[queryInd].lower()) - 97
        
        if bucket in vowelBucketInds:
            bucketOptions = vowelBucketInds
        else:
            bucketOptions = {bucket}

        bestOption = 5001

        for bucketOption in bucketOptions:
            if self.buckets[bucketOption] != None:
                op = self.buckets[bucketOption].getBestMatch(query, queryInd + 1)
                bestOption = min(bestOption, op)

        return bestOption


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        existingWords = set(wordlist)
        lowercaseToRealWord = {}
        vowelTree = TrieNode()

        for wordInd in range(len(wordlist)):
            word = wordlist[wordInd]
            if word.lower() not in lowercaseToRealWord:
                lowercaseToRealWord[word.lower()] = word
            
            vowelTree.addWord(wordlist, wordInd, 0)
        
        answers = []

        for query in queries:
            ans = ""
            if query in existingWords:
                ans = query
            elif query.lower() in lowercaseToRealWord:
                ans = lowercaseToRealWord[query.lower()]
            else:
                match = vowelTree.getBestMatch(query, 0)
                if match < len(wordlist):
                    ans = wordlist[match]
            
            answers.append(ans)

        return answers