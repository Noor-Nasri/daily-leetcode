class LinkedNode {
public:
    int key;
    int val;
    LinkedNode* prev;
    LinkedNode* next;

    LinkedNode(int key, int val){
        this->key = key;
        this->val = val;
        this->prev = NULL;
        this->next = NULL;
    }

};

class LRUCache {
    // The hard part is knowing which element has oldest get call/put, for evict
    // Which must run in O(1), cuz it can be at capacity and keep putting
    
    // So, which we get/put an element, it should be moved to the front of list
    // When we evict, we get rid of last element with pop

    // Very easy with doubly linked list

public:
    unordered_map<int, LinkedNode*> cached_values;
    LinkedNode* head = NULL;
    LinkedNode* tail = NULL;
    int capacity;
    int size;

    LRUCache(int capacity) {
        this->capacity = capacity;
        this->size = 0;
    }
    
    void updateRecent(LinkedNode* node){
        // push node to tail
        if (node == tail) return;

        if (node == head){
            // update head
            head = node->next; 
        }else{
            // unlink other nodes pointing to this
            node->prev->next = node->next; 
        }
        node->next->prev = node->prev;

        // fix node pointers
        node->prev = tail; 
        node->next = NULL;

        // update tail
        tail->next = node; 
        tail = node;
    }


    int get(int key) {
        if (!cached_values.count(key)) return -1;

        // update it to be most recent (tail), then return
        LinkedNode* node = cached_values[key];
        updateRecent(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (capacity == 0) return; // why bother
        if (cached_values.count(key)){
            LinkedNode* node = cached_values[key];
            node->val = value;
            updateRecent(node);
            return;
        }

        LinkedNode* node = new LinkedNode(key, value);
        cached_values[key] = node;
        size++;
        
        if (size == 1){
            head = node;
            tail = node;
            return;
        }

        // Put the element at the end of the list
        node->prev = tail;
        tail->next = node;
        tail = node;

        // remove oldest (head) if needed
        if (size > capacity){
            size--;
            LinkedNode* oldest = head;
            oldest->next->prev = NULL;
            head = oldest->next;
            
            cached_values.erase(oldest->key);
            delete oldest;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */