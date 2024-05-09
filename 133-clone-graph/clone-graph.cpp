/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == NULL) return NULL;

        //cout << "Starting with " << node << " \n";
        // First, I do graph search to make value copies
        unordered_map<Node*, Node*> cloneMappings;
        stack<Node*> remaining;
        remaining.push(node);
    
        while (!remaining.empty()){
            Node* next_node = remaining.top();
            remaining.pop();

            if (cloneMappings.count(next_node)) continue;
            Node* newNode = new Node(next_node->val);
            //cout << "Created copy for " << next_node->val << " \n";

            cloneMappings[next_node] = newNode;
            
            for (Node* old_node : next_node->neighbors){
                remaining.push(old_node);
            }
        }

        // Now I iterate over all copies, and make them match the connections
        for(auto it: cloneMappings){
            Node* old_pointer = it.first;
            Node* new_pointer = it.second;

            for (Node* old_neighbour : old_pointer->neighbors){
                Node* new_neighbour = cloneMappings[old_neighbour];
                new_pointer->neighbors.push_back(new_neighbour);                
                //cout << "Added edge: " << new_pointer->val << " to " << new_neighbour->val<< '\n';
            }
        }

        return cloneMappings[node];
    }
};














