class Node {
public:
    Node* left;
    Node* right;
    int val;
    Node(int value, Node* left, Node* right){
        this->val = value;
        this->left = left;
        this->right = right;
    }
};

class MyCircularDeque {
    Node* head;
    Node* tail;
    int numVals = 0;
    int maxVals = 0;

public:
    MyCircularDeque(int k) {
        this->maxVals = k;
        this->head = NULL;
        this->tail = NULL;
    }
    
    bool insertFront(int value) {
        if (numVals == maxVals) return false;
        if (this->head == NULL){
            this->head = new Node(value, NULL, NULL);
            this->tail = this->head;
            this->numVals = 1;
            return true;
        }

        Node* nextNode = new Node(value, NULL, this->head);
        this->head->left = nextNode;
        this->head = nextNode;
        this->numVals++;
        return true;
    }
    
    bool insertLast(int value) {
        if (numVals == maxVals) return false;
        if (this->head == NULL){
            this->head = new Node(value, NULL, NULL);
            this->tail = this->head;
            this->numVals = 1;
            return true;
        }

        Node* nextNode = new Node(value, this->tail, NULL);
        this->tail->right = nextNode;
        this->tail = nextNode;
        this->numVals++;
        return true;
    }
    
    bool deleteFront() {
        if (this->head == NULL) return false;

        if (this->head->right != NULL){
            this->head->right->left = NULL;
        }
        this->head = this->head->right;
        if (this->head == NULL){
            this->tail = NULL;
        }
        this->numVals--;
        return true;
    }
    
    bool deleteLast() {
        if (this->tail == NULL) return false;

        if (this->tail->left != NULL){
            this->tail->left->right = NULL;
        }
        this->tail = this->tail->left;
        if (this->tail == NULL){
            this->head = NULL;
        }
        this->numVals--;
        return true;
    }
    
    int getFront() {
        if (this->head == NULL) return -1;
        return this->head->val;
    }
    
    int getRear() {
        if (this->tail == NULL) return -1;
        return this->tail->val;
    }
    
    bool isEmpty() {
        return numVals == 0;
        
    }
    
    bool isFull() {
        return numVals == maxVals;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */