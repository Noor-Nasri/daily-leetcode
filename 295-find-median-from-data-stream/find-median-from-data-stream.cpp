class MedianFinder {
public:
    int numElements;
    pair<int, int> partitionSizes;
    int median; // value at position (n // 2). Even -> average it with smaller.
    vector<int> smaller; // max heap
    vector<int> bigger; // min heap

    MedianFinder() {
        numElements = 0;
        partitionSizes = {0, 0};
        median = -1;
        smaller = {};
        bigger = {};

        make_heap(smaller.begin(), smaller.end()); 
        make_heap(bigger.begin(), bigger.end(), greater<>{}); 
    }
    
    void addNum(int num) {
        numElements++;
        if (numElements == 1){
            median = num;
            return;
        }

        if (num <= median){
            // put in smaller
            partitionSizes.first++;
            smaller.push_back(num);
            push_heap(smaller.begin(), smaller.end());
        }else{
            // Put in bigger
            partitionSizes.second++;
            bigger.push_back(num);
            push_heap(bigger.begin(), bigger.end(), greater<>{});
        }

        if (partitionSizes.second > partitionSizes.first){
            // Shift median to smaller
            smaller.push_back(median);
            push_heap(smaller.begin(), smaller.end());
            partitionSizes.first++;

            median = bigger.front();
            pop_heap(bigger.begin(), bigger.end(), greater<>{});
            bigger.pop_back();
            partitionSizes.second--;
            
            
        }else if (partitionSizes.first > partitionSizes.second + 1){
            // Shift median to bigger
            bigger.push_back(median);
            push_heap(bigger.begin(), bigger.end(), greater<>{});
            partitionSizes.second++;

            median = smaller.front();
            pop_heap(smaller.begin(), smaller.end());
            smaller.pop_back();
            partitionSizes.first--;
        }

        //cout << "After adding in " << num << " we have " << numElements << " Elements and median: " << median << '\n';
        return;
    }
    
    double findMedian() {
        if (numElements % 2 == 1) return median;

        double avg = (median + smaller.front())/2.0;
        return avg;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */