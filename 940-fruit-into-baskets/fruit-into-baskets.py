class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Basic 2p window: expand till 3 colours, then shrink again till 2
        fruitCounts = {}
        left = 0
        right = -1
        best = -1

        while right < len(fruits) - 1:
            while right < len(fruits) - 1:
                if len(fruitCounts) == 2 and fruits[right + 1] not in fruitCounts:
                    break

                right += 1
                fruit = fruits[right]
                fruitCounts[fruit] = fruitCounts.get(fruit, 0) + 1
            
            numPicked = right - left + 1
            best = max(best, numPicked)
            
            while len(fruitCounts) > 1:
                fruit = fruits[left]
                if fruitCounts[fruit] == 1:
                    del fruitCounts[fruit] 
                else:
                    fruitCounts[fruit] -= 1
                
                left += 1

        return best