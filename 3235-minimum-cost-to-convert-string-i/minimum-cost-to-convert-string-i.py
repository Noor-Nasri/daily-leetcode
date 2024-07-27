class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # The point of the question is to be able to know best path char->char
        # ie, a -> b is a -> c -> b. Therefore just shortest path. Same daily as yesterday ..

        connections = {}
        for i in range(len(original)):
            org = ord(original[i]) - ord('a')
            tar = ord(changed[i]) - ord('a')
            c = cost[i]
            if not ((org, tar) in connections) or c < connections[(org, tar)]:
                connections[(org, tar)] = c
        
        # now treat it like a normal graph. Up to 26 nodes, simple O(n^3) solving dists
        for jump_node in range(26):
            for start_node in range(26):
                for target_node in range(26):
                    if not (start_node, jump_node) in connections or not (jump_node, target_node) in connections:
                        continue
                    
                    # found a way to connect two nodes
                    c = connections[(start_node, jump_node)] + connections[(jump_node, target_node)]
                    if not ((start_node, target_node) in connections) or c < connections[(start_node, target_node)]:
                        connections[(start_node, target_node)] = c 

        # Now simple solve
        total = 0
        for i in range(len(source)):
            org = ord(source[i]) - ord('a')
            tar = ord(target[i]) - ord('a')
            if org == tar:
                continue

            if not (org, tar) in connections:
                return -1
            
            total += connections[(org, tar)]


        return total