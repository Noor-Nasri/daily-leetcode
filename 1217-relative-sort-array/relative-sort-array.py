class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        important = set(arr2)
        counts = {}
        list2 = []
        for item in arr1:
            if not item in important:
                list2.append(item)
                continue
            
            if not item in counts:
                counts[item] = 1
            else:
                counts[item] += 1

        solution = []
        for item in arr2:
            for rep in range(counts[item]):
                solution.append(item)
        
        solution += sorted(list2)
        return solution
        