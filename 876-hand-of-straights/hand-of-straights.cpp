class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (groupSize == 1) return true;
        sort(hand.begin(), hand.end());
        
        // We will do this in a single pass by storing current hands
        // Since duplicates exist, slightly more complex greedy
        // We store a hand as {start_of_hand, num_dupes}
        // O(n) as the queue operations are O(1)

        int lastNum = -1;
        int totalRequired = 0;
        queue<pair<int, int>> curHands = {};

        for (int ind = 0; ind < hand.size(); ind++){
            int num = hand[ind];
            if (totalRequired && lastNum >= 0 && num - lastNum != 1) return false; // Can't continue existing hands

            int num_start = ind;
            while ((ind < hand.size() - 1) && (hand[ind + 1] == num)) ind++;
            int num_end = ind + 1;

            int count = num_end - num_start;
            if (count < totalRequired) return false;

            pair<int, int>& oldest = curHands.front();
            if (oldest.first == num - groupSize + 1){
                totalRequired -= oldest.second; // First x hands are done now
                count -= oldest.second;
                curHands.pop();
            }

            int newHands = count - totalRequired;
            if (newHands){
                totalRequired += newHands;
                curHands.push({num, newHands});
            }

            lastNum = num;
        }

        return curHands.empty();
    }
};