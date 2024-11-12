class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key = lambda x : x[0])
        results = [0 for i in range(len(queries))]
        new_queries = sorted([(queries[i], i) for i in range(len(queries))])
        
        item_index = 0
        best_beuty = 0

        for price, ind in new_queries:
            while (item_index < len(items) and items[item_index][0] <= price):
                best_beuty = max(best_beuty, items[item_index][1])
                item_index += 1
            results[ind] = best_beuty
        
        return results

