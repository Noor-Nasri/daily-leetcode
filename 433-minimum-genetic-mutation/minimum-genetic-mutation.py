class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        genes = ['A', 'C', 'G', 'T']
        quickBank = set(bank)
        if not (endGene in quickBank): return -1

        seen = set()
        seen.add(startGene)
        cur = [startGene]
        numEdits = 0

        while cur:
            next_round = []
            for gene in cur:
                if gene==endGene:
                    return numEdits
                
                for i in range(8):
                    for g in genes:
                        new_str = gene[:i] + g + gene[i+1:]
                        if not (new_str in seen) and new_str in quickBank:
                            seen.add(new_str)
                            next_round.append(new_str)

            numEdits += 1
            cur = next_round


        
        return -1

        