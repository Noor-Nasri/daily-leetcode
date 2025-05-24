class Solution:
    def solveMax(self, rootInd, parentInd, parentAppliedXor):
        uid = (rootInd, parentAppliedXor)
        if uid in self.sols:
            return self.sols[uid]
        
        total_base = 0
        bonus_from_xors = []
        losses_from_xors = []

        for childInd in self.connections[rootInd]:
            if childInd == parentInd:
                continue
            
            childSum = self.solveMax(childInd, rootInd, False)
            total_base += childSum

            xoredSum = self.solveMax(childInd, rootInd, True)
            child_delta = xoredSum - childSum

            if child_delta >= 0:
                bonus_from_xors.append(child_delta)
            else:
                losses_from_xors.append(-child_delta)

        children_bonus = sum(bonus_from_xors)

        # Now two options: keep this, or add/remove an xor
        self_values = [self.nums[rootInd] , self.nums[rootInd] ^ self.k]
        has_xor = int((int(parentAppliedXor) + len(bonus_from_xors)) % 2 == 1)
        option1 = self_values[has_xor] 
        
        option2 = -9999999
        if bonus_from_xors:
            possible = -min(bonus_from_xors) + self_values[1 - has_xor]
            option2 = max(option2, possible)
        
        if losses_from_xors:
            possible = -min(losses_from_xors) + self_values[1 - has_xor]
            option2 = max(option2, possible)

        adjustmentValue = max(option1, option2)

        total = total_base + children_bonus + adjustmentValue
        self.sols[uid] = total
        return self.sols[uid]

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        connections = [[] for i in range(len(nums))]
        for u, v in edges:
            connections[u].append(v)
            connections[v].append(u)
        
        root = None
        for ind in range(len(nums)):
            if len(connections[ind]) == 1:
                root = ind
                break
        
        self.nums = nums
        self.connections = connections
        self.k = k
        self.sols = {}
        return self.solveMax(root, None, False)
        