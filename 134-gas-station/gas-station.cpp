class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        // edge case check
        if (gas.size() == 1){
            return (gas[0] >= cost[0] ? 0 : -1);
        }

        int starting = 0;
        int current = 0;
        int total = 0;

        while (true){
            total += gas[current] - cost[current];
            if (total < 0){
                if (starting > current){
                    // already did a loop through, so none can be starting
                    return -1; 
                }

                starting = current + 1;
                current = starting;
                total = 0;
            } else{
                current = (current + 1) % gas.size();

                if (current == starting){
                    return starting;
                }
            }

        }

        return -1;;
    }
};