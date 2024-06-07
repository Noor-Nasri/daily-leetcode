class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        roots = set(dictionary)

        for ind in range(len(words)):
            for root_len in range(1, len(words[ind])):
                root = words[ind][:root_len]

                if (root in roots):
                    words[ind] = root
                    break
        
        return " ".join(words)



        