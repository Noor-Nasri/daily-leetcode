from heapq import heappush, heappop

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        queries = sorted(
            [ 
            [max(queries[i]), min(queries[i]), i]  
            for i in range(len(queries))
            ], reverse = True)

        solutions = [-1 for i in range(len(queries))]

        # Solve the queries at the same time while going through heights
        cur_waiting_to_connect = []
        cur_ind = 0
        while (cur_ind < len(heights)):
            # Add all queries that are now possible to satisfy
            while queries and queries[-1][0] == cur_ind:
                ind_second, ind_first, ind_q = queries.pop()
                if ind_first == ind_second or heights[ind_first] < heights[ind_second]:
                    solutions[ind_q] = ind_second
                else:
                    heappush(cur_waiting_to_connect, (heights[ind_first] + 1, ind_q))
            
            # Pop all queries that can land in this building
            while cur_waiting_to_connect and  heights[cur_ind] >= cur_waiting_to_connect[0][0]:
                h_needed, ind_q = heappop(cur_waiting_to_connect)
                solutions[ind_q] = cur_ind

            cur_ind += 1
        
        return solutions
