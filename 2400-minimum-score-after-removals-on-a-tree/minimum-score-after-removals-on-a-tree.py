from typing import List
from collections import defaultdict
# another public sol, just dont have time nowadays. 
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        xor = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        time = 0

        # Step 1: DFS to compute xor and timestamps
        def dfs(u, parent):
            nonlocal time
            xor[u] = nums[u]
            in_time[u] = time
            time += 1
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)
                xor[u] ^= xor[v]
            out_time[u] = time

        dfs(0, -1)
        total_xor = xor[0]

        def is_descendant(u, v):
            return in_time[v] < in_time[u] < out_time[u] <= out_time[v]

        # Step 2: Find children nodes for each edge
        edge_nodes = []
        for u, v in edges:
            if in_time[u] > in_time[v]:
                edge_nodes.append(u)
            else:
                edge_nodes.append(v)

        res = float('inf')
        m = len(edge_nodes)
        for i in range(m):
            for j in range(i + 1, m):
                a = edge_nodes[i]
                b = edge_nodes[j]

                if is_descendant(a, b):
                    x = xor[a]
                    y = xor[b] ^ xor[a]
                    z = total_xor ^ xor[b]
                elif is_descendant(b, a):
                    x = xor[b]
                    y = xor[a] ^ xor[b]
                    z = total_xor ^ xor[a]
                else:
                    x = xor[a]
                    y = xor[b]
                    z = total_xor ^ x ^ y

                res = min(res, max(x, y, z) - min(x, y, z))

        return res