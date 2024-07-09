class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        int curTime = 0;
        double runningAverage = 0;
        double numValues = 0;

        for (vector<int> & customer : customers){
            int arrival = customer[0];
            int duration = customer[1];

            if (curTime <= arrival){
                curTime = arrival + duration;
            }else{
                curTime += duration;
            }

            numValues += 1;
            int extraWait = curTime - arrival;
            runningAverage = (numValues - 1)/numValues * runningAverage + (1 / numValues) * extraWait;
            //cout << "Waited: " << extraWait << ", average is now: " << runningAverage << "\n";
        }

        return runningAverage;
        
    }
};