class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # We want start (xor) ... (xor) end
        # Can instead do [0] (xor) .. (xor) end (xor) [0] (xor) ... (xor) [start - 1]
        # this will cancel out the first start - 1 vars, because (a XOR b XOR b) = a

        xor_prefixsums = [arr[0]]
        for ind in range(1, len(arr)):
            xor_prefixsums.append(xor_prefixsums[-1] ^ arr[ind])
        results = []
        for s, e in queries:
            if s > 0:
                results.append(xor_prefixsums[e] ^ xor_prefixsums[s - 1])
            else:
                results.append(xor_prefixsums[e])
        
        return results