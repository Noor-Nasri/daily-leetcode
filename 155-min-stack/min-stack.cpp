class MinStack {
public:
    stack<int> values;
    stack<int> minValues;

    MinStack() {
        this->values = {};
        this->minValues = {};
    }
    
    void push(int val) {
        values.push(val);

        if (minValues.empty() || val <= minValues.top()){
            minValues.push(val);
        }
    }
    
    void pop() {
        int val = values.top();
        values.pop();

        if (minValues.top() == val){
            minValues.pop();
        }
    }
    
    int top() {
        return values.top();
    }
    
    int getMin() {
        return minValues.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */