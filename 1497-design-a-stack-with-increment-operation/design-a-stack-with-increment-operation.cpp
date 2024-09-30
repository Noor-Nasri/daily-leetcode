class CustomStack {
public:
    stack<int> baseVals = {};
    unordered_map<int, int> increments = {};
    int maxSize = 0;

    CustomStack(int maxSize) {
        this->maxSize = maxSize;
        // for (int i = 0; i < 1001; i++) increments[i] = 0;
    }
    
    void push(int x) {
        if (baseVals.size() < maxSize) baseVals.push(x);
    }
    
    int pop() {
        if (baseVals.empty()) return -1;
        int bonus = 0;
        if (increments.find(baseVals.size()) != increments.end()){
            bonus = increments[baseVals.size()];
            // now shift bonus to older elements

            if (increments.find(baseVals.size() - 1) != increments.end()){
                increments[baseVals.size() - 1] += increments[baseVals.size()];
            }else{
                increments[baseVals.size() - 1] = increments[baseVals.size()];
            }

            increments.erase(baseVals.size());
        }

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