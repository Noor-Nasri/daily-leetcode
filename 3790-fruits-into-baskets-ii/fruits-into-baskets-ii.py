class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for ind_f in range(len(fruits)):
            matched = False
            for ind_b in range(len(baskets)):
                if baskets[ind_b] >= fruits[ind_f]:
                    baskets[ind_b] = 0
                    matched = True
                    break

            if not matched:
                unplaced += 1

        return unplaced
        