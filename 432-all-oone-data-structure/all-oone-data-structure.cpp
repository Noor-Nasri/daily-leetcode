class Node {
    public:
    unordered_set<string> keys;
    int level = 0;
    Node* next;
    Node* prev;

    Node(int level, Node* prev, Node* next){
        this->level = level;   
        this->next = next;
        this->prev = prev;

        if (prev != NULL){
            prev->next = this;
        } 

        if (next != NULL){
            next->prev = this;
        }
    }
};

class AllOne {
public:
    unordered_map<string, Node*> nodeLocations;
    Node* head;
    Node* tail;
    AllOne() {
        this->head = NULL;
        this->tail = NULL;
        this->nodeLocations = {};
    }

    void delNode(Node* curNode){
        if (curNode == head && head == tail){
            head = NULL;
            tail = NULL;
            return;
        }

        Node *oldPrev = curNode->prev;
        Node *oldNext = curNode->next;
        if (oldPrev != NULL) oldPrev->next = oldNext;
        if (oldNext != NULL) oldNext->prev = oldPrev;
        if (curNode == head) head = head->next;
        if (curNode == tail) tail = tail->prev;
    }
    
    void inc(string key) {
        if (head == NULL){
            // case 0: empty list
            head = new Node(1, NULL, NULL);
            tail = head;
            nodeLocations[key] = head;
            nodeLocations[key]->keys.insert(key);
            return;
        }

        if (nodeLocations.find(key) == nodeLocations.end() || nodeLocations[key] == NULL){
            // if it does not exist, put it at level 0 first
            head = new Node(0, NULL, head);
            nodeLocations[key] = head;
            head->keys.insert(key);
        }
        
        Node *curNode = nodeLocations[key];
        curNode->keys.erase(key);
        if (curNode == tail){
            // case 1: tail, make new node
            tail = new Node(tail->level + 1, tail, NULL);
            nodeLocations[key] = tail;

        } else if (curNode->level + 1 == curNode->next->level){
            // case 2: right node is what we want
            nodeLocations[key] = curNode->next;

        } else {
            // case 3: we need a new middle node
            nodeLocations[key] = new Node(curNode->level + 1, curNode, curNode->next);
        }

        nodeLocations[key]->keys.insert(key);
        if (curNode->keys.empty()) delNode(curNode);
    }
    
    void dec(string key) {
        // constraints: key already exists, so not empty
        Node *curNode = nodeLocations[key];
        curNode->keys.erase(key);
        if (curNode == head){
            if (curNode->level == 1){
                // case 0: delete string entirely
                nodeLocations[key] = NULL;
            }else{
                // case 1: new head
                head = new Node(head->level - 1, NULL, head);
                nodeLocations[key] = head;
            }
            
        } else if (curNode->level - 1 == curNode->prev->level){
            // case 2: left node is what we want
            nodeLocations[key] = curNode->prev;

        } else {
            // case 3: we need a new middle node
            nodeLocations[key] = new Node(curNode->level - 1, curNode->prev, curNode);
        }

        if (nodeLocations[key] != NULL) nodeLocations[key]->keys.insert(key);
        if (curNode->keys.empty()) delNode(curNode);
    }
    
    string getMaxKey() {
        if (head == NULL) return "";
        return *(tail->keys.begin());
    }
    
    string getMinKey() {
        if (head == NULL) return "";
        return *(head->keys.begin());
        
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */