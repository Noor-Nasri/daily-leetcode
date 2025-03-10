class Solution:
    def checkStatus(self, counts, k):
        if counts["rest"] > k:
            return "Invalid"

        elif counts["rest"] < k:
            return "Incomplete"

        for let in ["a", "e", "i", "o", "u"]:
            if not counts[let]:
                return "Incomplete"
        
        return "Valid"

    def adjustLetter(self, counts, letter, k, inc):
        key = letter in counts and letter or "rest"
        counts[key] += inc
        return self.checkStatus(counts, k)


    def countOfSubstrings(self, word: str, k: int) -> int:
        counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "rest": 0}
        ind_next_consonant = [len(word) for i in range(len(word))]
        for ind in range(len(word) - 2, -1, -1):
            if word[ind + 1] not in counts:
                ind_next_consonant[ind] = ind + 1
            else:
                ind_next_consonant[ind] = ind_next_consonant[ind + 1]

        total_found = 0
        ind_s = 0
        ind_e = 0

        while ind_e < len(word):
            letter = word[ind_e]
            status = self.adjustLetter(counts, letter, k, 1)

            while status == "Invalid":
                status = self.adjustLetter(counts, word[ind_s], k, -1)
                ind_s += 1

            numSameSubstrs = ind_next_consonant[ind_e] - ind_e
            while status == "Valid":
                #print(ind_s, ind_e, "results in", numSameSubstrs, "answers")
                total_found += numSameSubstrs
                status = self.adjustLetter(counts, word[ind_s], k, -1)
                ind_s += 1

            ind_e += 1

        
        return total_found