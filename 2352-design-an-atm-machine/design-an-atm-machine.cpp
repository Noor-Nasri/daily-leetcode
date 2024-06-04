class ATM {
public:
    int values[5] = {20, 50, 100, 200, 500};
    int notes[5] = {0, 0, 0, 0, 0};
    ATM() {
    }
    
    void deposit(vector<int> banknotesCount) {
        for (int i = 0; i < 5; i++){
            notes[i] += banknotesCount[i];
        }
    }
    
    vector<int> withdraw(int amount) {
        int remaining = amount;
        vector<int> noteChoices = {0, 0, 0, 0, 0};
        for (int i = 4; i >= 0; i--){
            int notesNeeded = min(notes[i], remaining / values[i]);
            noteChoices[i] = notesNeeded;
            remaining -= notesNeeded * values[i];
        }
        
        if (remaining != 0) return {-1};

        // update and return 
        for (int i = 0; i < 5; i++) notes[i] -= noteChoices[i];
        return noteChoices;
    }
};

/**
 * Your ATM object will be instantiated and called as such:
 * ATM* obj = new ATM();
 * obj->deposit(banknotesCount);
 * vector<int> param_2 = obj->withdraw(amount);
 */