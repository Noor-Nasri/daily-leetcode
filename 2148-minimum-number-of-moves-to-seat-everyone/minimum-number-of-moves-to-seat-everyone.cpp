class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        int total_moves = 0;
        sort(seats.begin(), seats.end());
        sort(students.begin(), students.end());

        for (int ind = 0; ind < seats.size(); ind++){
            total_moves += abs(seats[ind] - students[ind]);
        }

        return total_moves;
        
    }
};