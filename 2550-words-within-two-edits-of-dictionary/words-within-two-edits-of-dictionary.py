class Solution:
    # this question is worded bad. They mean we just change two inds. So just basic brute force to count mismatches ..

    def getDiff(self, query, word):
        return sum([int(query[i] != word[i]) for i in range(len(query))])
        
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        matched = []
        for query in queries:
            for word in dictionary:
                if self.getDiff(query, word) <= 2:
                    matched.append(query)
                    break

        return matched
        