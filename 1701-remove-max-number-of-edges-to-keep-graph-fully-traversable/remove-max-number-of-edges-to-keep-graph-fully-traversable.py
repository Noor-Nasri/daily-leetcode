class Solution:
    def makeGroup(self, connections, groupings, index, group_new):
        total_edges = 0
        for vertex in connections[index]:
            if groupings[vertex] == group_new: 
                continue # can already reach this node, ignore edge
            
            groupings[vertex] = group_new
            total_edges += 1
            total_edges += self.makeGroup(connections, groupings, vertex, group_new)
        return total_edges
    
    def improveReach(self, connections, all_groups, cur_index, reachable):
        for vertex in all_groups[cur_index]:
            for conn in connections[vertex]:
                reachable.add(conn)

    def connectGroups(self, connections, all_groups):
        for group_ind in all_groups:
            if group_ind == 0: # First group always 0, dont need to match
                reachable = set()
                numEdges = 0
                self.improveReach(connections, all_groups, 0, reachable)
                continue 
            
            found_connection = False
            for vertex in all_groups[group_ind]:
                if vertex in reachable:
                    # Can connect this group to previous ones!
                    found_connection = True
                    break
            
            if found_connection:
                numEdges += 1
                self.improveReach(connections, all_groups, group_ind, reachable)
            else:
                return -1
        
        return numEdges


    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Seems complicated but it can be made simple ... just long
        # We just want to figure out the min number of edges that connect all vertices
        # It's always better to pick Type 3 cuz its more efficient
        # So first just solve for Type 3: get connected groups and remove extras within groups
        # Then for type 1 and 2, just see if you can merge the groups
        connections_alice = [[] for i in range(n)]
        connections_bob = [[] for i in range(n)]
        connections_both = [[] for i in range(n)]
        for t, u, v in edges:
            if t == 1:
                connections = connections_alice
            elif t == 2:
                connections = connections_bob
            else:
                connections = connections_both
            
            connections[u-1].append(v-1)
            connections[v-1].append(u-1)


        groupings = [i for i in range(n)] # all start detached
        edges_both = 0
        for i in range(n):
            if groupings[i] < i:
                continue # already put into an earlier group
            
            edges_both += self.makeGroup(connections_both, groupings, i, i)

        #print("Groupings result:", groupings, edges_both)
        all_groups = {}
        for ind, group in enumerate(groupings):
            if not group in all_groups:
                all_groups[group] = []
            all_groups[group].append(ind)

        #print("Becomes", all_groups)


        # now .. we have min edges kept to group as much as we can
        edges_alice = self.connectGroups(connections_alice, all_groups)
        #print(edges_alice)
        if edges_alice == -1: return -1

        edges_bob = self.connectGroups(connections_bob, all_groups)
        if edges_bob == -1: return -1

        total_edges = edges_both + edges_alice + edges_bob

        return len(edges) - total_edges
        