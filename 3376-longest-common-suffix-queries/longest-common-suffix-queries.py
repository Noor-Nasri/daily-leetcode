# Solution would definitely need some form of trie so that each query is efficient
# The tricky part is constructing the tree efficiently 
# I think this is pretty doable, build a trie through backwards traversal and mark each node to ind of smallest in length
# But its late now so we do public solution

class TrieNode:
    __slots__ = ['children', 'bestLen', 'bestIdx']
    
    def __init__(self):
        self.children = {}
        self.bestLen = float('inf')
        self.bestIdx = float('inf')

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        for i, word in enumerate(wordsContainer):
            n = len(word)
            curr = root
            
            if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                curr.bestLen = n
                curr.bestIdx = i
                
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
                
                if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                    curr.bestLen = n
                    curr.bestIdx = i
                    
        ans = []
        
        for query in wordsQuery:
            curr = root
            
            for char in reversed(query):
                if char not in curr.children:
                    break
                curr = curr.children[char]
            
            ans.append(curr.bestIdx)
            
        return ans