class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        if len(sentence1) < len(sentence2):
            shorter = sentence1
            longer = sentence2
        else:
            shorter = sentence2
            longer = sentence1

        for ind in range(len(shorter)):
            if shorter[ind] == longer[ind]:
                continue
            
            # will need to add words here to fill the rest
            remaining_inds = len(shorter) - ind
            return longer[-remaining_inds:] ==  shorter[ind:]

        return True
        