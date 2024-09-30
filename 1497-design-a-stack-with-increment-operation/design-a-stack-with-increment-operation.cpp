class CustomStack {
public:
    stack<int> baseVals = {};
    unordered_map<int, int> increments = {};
    int maxSize = 0;

    CustomStack(int maxSize) {
        this->maxSize = maxSize;
        for (int i = 0; i < 1001; i++) increments[i] = 0;
    }
    
    void push(int x) {
        if (baseVals.size() < maxSize){
            baseVals.push(x);
        }
    }
    
    int pop() {
        if (baseVals.empty()) return -1;
        int bonus = increments[baseVals.size()];
        if (baseVals.size() > 0){
            increments[baseVals.size() - 1] += increments[baseVals.size()];
        }
        increments[baseVals.size()] = 0;
        int baseVal = baseVals.top();
        baseVals.pop();
        return baseVal + bonus;
    }
    
    void increment(int k, int val) {
        if (k > baseVals.size()){
            k = baseVals.size();
        }
        increments[k] += val;
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */